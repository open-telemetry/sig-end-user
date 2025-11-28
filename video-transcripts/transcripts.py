import os
import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
from youtube_transcript_api._errors import YouTubeRequestFailed
from dotenv import load_dotenv
from slugify import slugify
import json
import openai
import sys
import time
import random

load_dotenv()

# Env var setup
# If this first one is missing, run fails, which is good.
youtube_key = os.environ.get('API_KEY')
# Second one is optional, but if it's missing, we'll skip the summary and cleanup.
openai_key = os.environ.get("OPENAI_API_KEY","")

def _fetch_playlist_video_ids(youtube, playlist_id, max_pages=100):
    """
    Fetch all video IDs from a playlist with pagination and retry logic.
    @param youtube: YouTube API client instance
    @param playlist_id: YouTube playlist ID
    @param max_pages: Maximum number of pages to fetch
    @return: List of video IDs
    """
    video_ids = []
    next_page_token = None
    page_count = 0
    max_retries = 3
    retry_count = 0

    while page_count < max_pages:
        try:
            page_count += 1
            
            # Build request parameters
            request_params = {
                'part': 'snippet',
                'playlistId': playlist_id,
                'maxResults': 50
            }
            
            # Only add pageToken if it's not None
            if next_page_token:
                request_params['pageToken'] = next_page_token
                
            request = youtube.playlistItems().list(**request_params)
            response = request.execute()

            for item in response['items']:
                video_ids.append(item['snippet']['resourceId']['videoId'])
            
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
            
            # Reset retry count on successful request
            retry_count = 0
            
        except HttpError as e:
            if e.resp.status == 403 and 'quota' in str(e).lower():
                retry_count += 1
                if retry_count >= max_retries:
                    raise RuntimeError(f"Max retries ({max_retries}) exceeded due to quota limits")
                print(f"Quota exceeded while fetching playlist items (attempt {retry_count}/{max_retries}). Waiting before retry...")
                time.sleep(60)  # Wait 1 minute
                continue
            else:
                print(f"Error fetching playlist items: {e}")
                raise

    return video_ids


def _fetch_video_details_batch(youtube, video_ids):
    """
    Fetch detailed video information for a list of video IDs in batches.
    @param youtube: YouTube API client instance
    @param video_ids: List of YouTube video IDs
    @return: List of video objects with detailed information
    """
    videos = []
    batch_size = 50  # YouTube API allows up to 50 IDs per request
    max_retries = 3
    
    for i in range(0, len(video_ids), batch_size):
        batch_ids = video_ids[i:i + batch_size]
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                request = youtube.videos().list(
                    part='snippet',
                    id=','.join(batch_ids)
                )
                response = request.execute()
                
                for item in response['items']:
                    print(f"Found video: {item['snippet']['title']}")
                    videos.append(item)
                
                # Success - break out of retry loop and move to next batch
                break
                
            except HttpError as e:
                if e.resp.status == 403 and 'quota' in str(e).lower():
                    retry_count += 1
                    if retry_count >= max_retries:
                        print(f"Max retries ({max_retries}) exceeded on video details batch {i//batch_size + 1}")
                        break
                    print(f"Quota exceeded on video details batch {i//batch_size + 1} (attempt {retry_count}/{max_retries}). Waiting before retry...")
                    time.sleep(60)
                else:
                    print(f"Error fetching video details batch {i//batch_size + 1}: {e}")
                    break  # Don't retry on non-quota errors

    return videos


def get_playlist_videos(playlist_id, max_pages=100):
    """
    Fetch all videos from a YouTube playlist with their detailed information.
    @param playlist_id: YouTube playlist ID
    @param max_pages: Maximum number of pages to fetch (default 100)
    @return: List of video objects with detailed information
    """
    youtube = build('youtube', 'v3', developerKey=youtube_key)
    
    # Step 1: Get all video IDs from the playlist
    video_ids = _fetch_playlist_video_ids(youtube, playlist_id, max_pages)
    
    # Step 2: Fetch detailed information for each video
    videos = _fetch_video_details_batch(youtube, video_ids)
    
    return videos

def get_channel_videos(channel_id, start_date, end_date):
    youtube = build('youtube', 'v3', developerKey=youtube_key)
    
    videos = []
    next_page_token = None
    page_count = 0
    max_pages = 1  # Limit to 1 page (50 videos max) to avoid pagination issues

    while page_count < max_pages:
        try:
            # Build request parameters
            request_params = {
                'part': 'snippet',
                'channelId': channel_id,
                'maxResults': 50,
                'order': 'date',
                'type': 'video'
            }
            
            # Only add pageToken if it's not None
            if next_page_token:
                request_params['pageToken'] = next_page_token
                
            request = youtube.search().list(**request_params)
            print(f"Making API request with params: {request_params}")
            response = request.execute()
            print(f"API request successful, got {len(response.get('items', []))} videos")

            for item in response['items']:
                videos.append(item)            

            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
            
            page_count += 1
            
        except HttpError as e:
            if e.resp.status == 403 and 'quota' in str(e).lower():
                print("Quota exceeded while searching channel videos. Waiting before retry...")
                time.sleep(60)  # Wait 1 minute
                continue
            else:
                print(f"Error searching channel videos: {e}")
                raise
    
    return videos

def get_publish(video):
    snippet = video['snippet']

    if 'publishTime' in snippet:
        return snippet['publishTime']
    return snippet['publishedAt']

def get_id(video):
    if type(video['id']) == str:
        return video['id']
    
    return video['id']['videoId']

def fetch_transcripts(args, videos):
    processed = []
    for i, video in enumerate(videos):
        video_id = get_id(video)
        
        if video_id == '':
            print(f"Could not find video ID for video ")
            print(json.dumps(video, indent=2))
            continue

        if os.path.isfile(file_for_video(args, video)):
            print(f"Skipping video {video_id} because it already has a transcript.")
            continue

        print(f"Processing video {i+1}/{len(videos)}: {video_id}")
        
        # Use improved transcript fetching with retry logic
        transcript_text, raw_transcript = get_video_transcript_with_retry(video_id)
        
        if transcript_text:
            video['transcript'] = transcript_text
            video['raw_transcript'] = raw_transcript
            processed.append(video)
            write_markdown(args, video)
        else:
            print(f"Skipping video {video_id} due to transcript issues.")
            
        # Rate limiting prevention: Small delay between transcript fetches to avoid 
        # triggering YouTube's rate limits (429 errors). Better to wait 2-5 seconds 
        # proactively than 60-120 seconds reactively if rate limited.
        if i < len(videos) - 1:  # Don't sleep after the last video
            delay = random.uniform(2, 5)  # Random delay between 2-5 seconds
            print(f"Waiting {delay:.1f} seconds before next video...")
            time.sleep(delay)
    
    return processed

def file_for_video(args, video):
    """Determines a reasonable local filename for a given video.
    @param args: The command line arguments/user preferences
    @param video: The video object
    @return: A string containing a path to a slugified and dated filename
    """
    published = get_publish(video)
    
    if published == '':
        raise Exception("Could not find publish time for video")

    title = video['snippet']['title']
    slug = slugify(title)
    filename = f"{args.path}/{published}-{slug}.md"
    return filename

def get_video_transcript_with_retry(video_id, max_retries=5):
    """
    Fetch transcript with retry logic and exponential backoff.
    Uses youtube-transcript-api 1.2.3+ API.
    Handles YouTube rate limiting (429 errors) with extended wait times (60-120 seconds).
    Returns a tuple: (cleaned transcript text, raw transcript data) or (None, None) if unavailable.
    """
    for attempt in range(max_retries):
        try:
            # Use youtube-transcript-api 1.x API
            transcript_api = YouTubeTranscriptApi()
            fetched_transcript = transcript_api.fetch(
                video_id, 
                languages=['en', 'es', 'fr', 'de', 'ja']
            )
            # Convert to list of dicts format
            transcript = fetched_transcript.to_raw_data()
            
            # Validate transcript structure
            if not transcript or not isinstance(transcript, list):
                print(f"Invalid transcript format for video {video_id}")
                return None, None
                
            # Safely extract and clean text
            text_parts = []
            for entry in transcript:
                if isinstance(entry, dict) and 'text' in entry:
                    text = entry['text']
                    if text and isinstance(text, str):
                        text = text.strip()
                        # Filter out common non-content entries
                        if text and text not in ['[Music]', '[Applause]', '[Laughter]']:
                            text_parts.append(text)
            
            if not text_parts:
                print(f"No valid text found in transcript for video {video_id}")
                return None, None
                
            full_text = ' '.join(text_parts)
            
            # Minimum length validation
            if len(full_text.strip()) < 50:
                print(f"Transcript too short for video {video_id}: {len(full_text)} characters")
                return None, None
                
            return full_text, transcript
            
        except TranscriptsDisabled:
            print(f"Transcripts are disabled for video {video_id}")
            return None, None
        except NoTranscriptFound:
            print(f"No transcript found for video {video_id}")
            return None, None
        except VideoUnavailable:
            print(f"Video {video_id} is unavailable")
            return None, None
        except YouTubeRequestFailed as e:
            error_str = str(e)
            if 'blocking requests from your IP' in error_str or 'IP has been blocked' in error_str:
                print(f"❌ YouTube IP block detected for video {video_id}")
                print(f"   See README 'YouTube IP Blocking' section for solutions")
                return None, None
            elif '429' in error_str or 'Too Many Requests' in error_str:
                if attempt < max_retries - 1:
                    wait_time = random.uniform(60, 120)
                    print(f"⚠️  Rate limit detected (429) - waiting {wait_time:.0f}s (retry {attempt + 2}/{max_retries})")
                    time.sleep(wait_time)
                else:
                    print(f"❌ Rate limit persists after {max_retries} attempts - wait 10-15 minutes and retry")
                    return None, None
            else:
                # Other YouTube API errors
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt) * 5 + random.uniform(0, 5)
                    print(f"YouTube API error for video {video_id}. Retrying in {wait_time:.1f}s...")
                    time.sleep(wait_time)
                else:
                    print(f"YouTube API error persists for video {video_id}: {str(e)}")
                    return None, None
        except Exception as e:
            error_str = str(e)
            # Check if this is likely a rate limit error disguised as XML parse error
            if 'no element found' in error_str or 'line 1, column 0' in error_str:
                if attempt < max_retries - 1:
                    wait_time = random.uniform(60, 120)
                    print(f"⚠️  Possible rate limit (XML parse error) - waiting {wait_time:.0f}s (retry {attempt + 2}/{max_retries})")
                    time.sleep(wait_time)
                else:
                    print(f"❌ Persistent error after {max_retries} attempts - see README troubleshooting")
                    return None, None
            elif attempt < max_retries - 1:
                # Standard exponential backoff for other errors
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                print(f"Attempt {attempt + 1} failed for video {video_id}. Retrying in {wait_time:.1f}s... Error: {error_str}")
                time.sleep(wait_time)
            else:
                print(f"All {max_retries} attempts failed for video {video_id}: {error_str}")
                return None, None
    
    return None, None

def openai_cleanup(transcript, video_id):
    """
    Take a messy raw YouTube transcript and return a concise summary + a cleaned up version.
    This only works if OPENAI_API_KEY is set in the environment. 
    @param transcript: The raw transcript of a YouTube video
    @return: A tuple containing the summary of the video and the cleaned up transcript
    """
    if openai_key == "":
        print("No OpenAI API key found in .env file; skipping summary and cleanup.")
        return ["Summary not available", None]

    client = openai.OpenAI(api_key=openai_key)

    summarize_pls = """
    You are a helpful assistant that summarizes YouTube transcripts.
    You will be given a transcript of a YouTube video, and you will need to summarize it.
    The summary should contain a brief overview of the subject matter of the video, names of people
    who were present, and a brief overview of the main points of the video and topics explored.  
    Make the summary no more than one paragraph
    """

    print(f"Summarizing transcript for video {video_id}")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": summarize_pls},
            {"role": "user", "content": transcript}
        ],
        temperature=0.7,
    )

    summary = response.choices[0].message.content

    cleanup_transcript_prompt = """
    You are a helpful assistant that cleans up YouTube transcripts. You will be given a messy
    transcript that contains few sentence breaks, indications of music in the video, and filler words.  
    You will need to clean up the transcript into a set of logical sentences and paragraphs.

    CRITICAL INSTRUCTIONS:
    - Use the EXACT words from the original transcript - do not paraphrase or rewrite
    - ONLY remove filler words like "um", "uh", "ah", "you know", "like" (when used as filler), "so" (when used as filler)
    - Fix sentence structure by adding proper punctuation and paragraph breaks
    - Do NOT change technical terms, names, or any substantive content
    - Do NOT summarize or condense - keep all the original content
    - Do NOT add words that weren't in the original
    - If someone repeats themselves, keep the repetition
    - Preserve the natural speaking style and word choice of each speaker

    SPEAKER FORMATTING:
    - Identify when different speakers are talking
    - Format speaker names as **Name:** at the start of their dialogue
    - Use bold ONLY for speaker names, not for emphasis or highlighting other text
    - Each time a speaker changes, start a new paragraph with their name
    - Keep the same speaker name format throughout (e.g., if someone introduces themselves as "Jacob Marino", use **Jacob:** consistently)

    OUTPUT FORMAT:
    - Use markdown paragraph breaks (blank lines) between speakers
    - Do NOT use bold, italic, or other formatting except for speaker names
    - Do NOT add bullets or numbered lists unless they were explicitly spoken
    - Keep it simple: speaker names in bold, everything else as plain text
    """

    print(f"Cleaning up transcript for video {video_id}")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": cleanup_transcript_prompt},
            {"role": "user", "content": transcript}
        ],
        temperature=0.7,
    )
    cleaned_up = response.choices[0].message.content

    return [summary, cleaned_up]

def clean_ai_preamble(text):
    """
    Remove AI assistant preamble lines from the response, keeping only the actual content.
    This strips lines like "Sure! Here are the key moments..." or "Here are 10 key moments..."
    @param text: The raw text response from AI
    @return: Cleaned text with only the actual chapter timestamps
    """
    if not text:
        return text
    
    lines = text.split('\n')
    cleaned_lines = []
    
    # Common preamble patterns to remove
    preamble_patterns = [
        'sure!',
        'here are',
        'here\'s',
        'below are',
        'i\'ve identified',
        'i have identified',
        'key moments',
        'from the livestream',
        'from the transcript',
        'from the youtube',
        'with timestamps',
        'along with their timestamps',
        'with their timestamps',
        'with the corresponding timestamps'
    ]
    
    for line in lines:
        line_lower = line.lower().strip()
        
        # Skip empty lines at the start, but keep them later for formatting
        if not cleaned_lines and not line_lower:
            continue
            
        # Check if this line is a preamble (contains preamble patterns and doesn't look like a timestamp)
        is_preamble = False
        if line_lower and not line_lower.startswith('0'):  # Timestamps start with 0
            for pattern in preamble_patterns:
                if pattern in line_lower:
                    is_preamble = True
                    break
        
        if not is_preamble:
            cleaned_lines.append(line)
    
    # Remove leading empty lines from the result
    while cleaned_lines and not cleaned_lines[0].strip():
        cleaned_lines.pop(0)
    
    return '\n'.join(cleaned_lines)

def parse_timestamp_to_seconds(timestamp_str):
    """
    Convert a timestamp string like '00:05:30' to seconds (330).
    @param timestamp_str: String in format HH:MM:SS or MM:SS
    @return: Integer seconds
    """
    parts = timestamp_str.strip().split(':')
    if len(parts) == 3:
        hours, minutes, seconds = parts
        return int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    elif len(parts) == 2:
        minutes, seconds = parts
        return int(minutes) * 60 + int(seconds)
    return 0

def parse_chapters(chapters_text):
    """
    Parse the chapters text into a list of (timestamp_seconds, timestamp_str, title) tuples.
    @param chapters_text: Text with lines like "00:05:30 Guest introduction"
    @return: List of tuples (seconds, timestamp_str, title)
    """
    chapters = []
    for line in chapters_text.split('\n'):
        line = line.strip()
        if not line:
            continue
        # Match timestamp at start of line (HH:MM:SS or MM:SS format)
        import re
        match = re.match(r'^(\d{1,2}:\d{2}:\d{2})', line)
        if match:
            timestamp_str = match.group(1)
            seconds = parse_timestamp_to_seconds(timestamp_str)
            title = line[len(timestamp_str):].strip()
            chapters.append((seconds, timestamp_str, title))
    return chapters

def insert_timestamps_in_transcript(cleaned_transcript, chapters, raw_transcript):
    """
    Insert timestamp markers into the cleaned transcript at appropriate positions.
    @param cleaned_transcript: The cleaned transcript text from OpenAI
    @param chapters: List of (seconds, timestamp_str, title) tuples
    @param raw_transcript: Raw transcript data from YouTube with timing info
    @return: Transcript with timestamps inserted
    """
    if not cleaned_transcript or not chapters or not raw_transcript:
        return cleaned_transcript
    
    # Build a mapping of time (in seconds) to text at that time
    # Store multiple entries per time window for better matching
    time_to_texts = {}
    for entry in raw_transcript:
        if isinstance(entry, dict) and 'text' in entry and 'start' in entry:
            text = entry['text'].strip()
            if text and text not in ['[Music]', '[Applause]', '[Laughter]']:
                start_time = int(entry['start'])
                if start_time not in time_to_texts:
                    time_to_texts[start_time] = []
                time_to_texts[start_time].append(text)
    
    # Split transcript into lines
    lines = cleaned_transcript.split('\n')
    
    # For each chapter, find the best line to insert it at
    line_to_chapter = {}  # Maps line index to (timestamp_str, title) to insert
    
    for seconds, timestamp_str, title in chapters:
        # Get text from a window around the timestamp (±5 seconds)
        window_texts = []
        for time_sec in range(max(0, seconds - 5), seconds + 6):
            if time_sec in time_to_texts:
                window_texts.extend(time_to_texts[time_sec])
        
        if not window_texts:
            # Fallback to closest time if window is empty
            closest_time = min(time_to_texts.keys(), 
                             key=lambda t: abs(t - seconds),
                             default=None)
            if closest_time:
                window_texts = time_to_texts[closest_time]
        
        if not window_texts:
            continue
        
        # Combine all texts in the window
        combined_text = ' '.join(window_texts)
        
        # Extract key words from the window text
        sample_words = [w.lower() for w in combined_text.split() 
                       if len(w) > 3 and w.lower() not in ['that', 'this', 'with', 'from', 'have', 'were', 'been', 'they', 'them']]
        
        if not sample_words:
            sample_words = [w.lower() for w in combined_text.split() if len(w) > 2][:10]
        
        # Also use words from the chapter title itself
        title_words = [w.lower() for w in title.split() 
                      if len(w) > 3 and w.lower() not in ['the', 'and', 'for', 'with', 'about', 'discussion', 'introduction']]
        
        # Find the best matching line in cleaned transcript
        best_line_idx = None
        best_score = 0
        
        for idx, line in enumerate(lines):
            # Skip empty lines and lines that already have chapter markers
            if not line.strip() or line.strip().startswith('###'):
                continue
            
            line_lower = line.lower()
            
            # Count matching words from the window
            text_matches = sum(1 for word in sample_words if word in line_lower)
            
            # Count matching words from the chapter title
            title_matches = sum(1 for word in title_words if word in line_lower) * 2  # Weight title matches more
            
            # Bonus for lines that start with speaker markers
            is_speaker_line = '**' in line and ':' in line
            speaker_bonus = 1 if is_speaker_line else 0
            
            # Prefer lines that appear after already-placed timestamps (chronological order)
            position_bonus = 0
            if line_to_chapter:
                last_placed = max(line_to_chapter.keys())
                if idx > last_placed:
                    position_bonus = 0.5
            
            score = text_matches + title_matches + speaker_bonus + position_bonus
            
            if score > best_score:
                best_score = score
                best_line_idx = idx
        
        # Insert chapter marker at the best matching line
        if best_line_idx is not None and best_score > 1:  # Require at least some confidence
            # Only insert if we don't already have a chapter marker for this line
            if best_line_idx not in line_to_chapter:
                line_to_chapter[best_line_idx] = (timestamp_str, title)
    
    # Build the result by inserting chapter headings before marked lines
    result_lines = []
    for idx, line in enumerate(lines):
        if idx in line_to_chapter:
            # Insert H3 heading before this line with timestamp and chapter title
            timestamp, title = line_to_chapter[idx]
            result_lines.append(f"### [{timestamp}] {title}")
            result_lines.append("")  # Add blank line after heading
            result_lines.append(line)
        else:
            result_lines.append(line)
    
    return '\n'.join(result_lines)

def format_duration(seconds):
    """
    Format seconds into HH:MM:SS format.
    @param seconds: Integer seconds
    @return: String in HH:MM:SS format
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def get_video_duration(raw_transcript):
    """
    Calculate the video duration from the raw transcript data.
    @param raw_transcript: Raw transcript data from YouTube with timing info
    @return: Duration in seconds, or None if unavailable
    """
    if not raw_transcript:
        return None
    
    max_time = 0
    for entry in raw_transcript:
        if isinstance(entry, dict) and 'start' in entry and 'duration' in entry:
            end_time = entry['start'] + entry['duration']
            max_time = max(max_time, end_time)
    
    return int(max_time) if max_time > 0 else None

def validate_and_fix_chapters(chapters_text, raw_transcript, video_id):
    """
    Validate that chapter descriptions match what's actually said at those timestamps.
    Fix any mismatches by finding the correct timestamp for the description.
    @param chapters_text: The generated chapters text
    @param raw_transcript: Raw transcript data with timing info
    @param video_id: The YouTube video ID
    @return: Validated and corrected chapters text
    """
    if openai_key == "" or not raw_transcript or not chapters_text:
        return chapters_text
    
    # Parse the chapters
    parsed = parse_chapters(chapters_text)
    if not parsed:
        return chapters_text
    
    print(f"Validating {len(parsed)} chapters for video {video_id}")
    
    # Build a map of timestamp to text and also create text segments
    time_to_text = {}
    all_segments = []  # List of (start_time, text) for searching
    
    for entry in raw_transcript:
        if isinstance(entry, dict) and 'text' in entry and 'start' in entry:
            text = entry['text'].strip()
            if text and text not in ['[Music]', '[Applause]', '[Laughter]']:
                start_time = int(entry['start'])
                if start_time not in time_to_text:
                    time_to_text[start_time] = []
                time_to_text[start_time].append(text)
                all_segments.append((start_time, text))
    
    client = openai.OpenAI(api_key=openai_key)
    validated_chapters = []
    
    for seconds, timestamp_str, title in parsed:
        # Skip 00:00:00 as it's typically correct
        if seconds == 0:
            validated_chapters.append(f"{timestamp_str} {title}")
            continue
        
        # Get text around the current timestamp (±10 seconds window)
        context_texts = []
        for time_sec in range(max(0, seconds - 10), seconds + 11):
            if time_sec in time_to_text:
                context_texts.extend(time_to_text[time_sec])
        
        if not context_texts:
            # If no text found, keep original
            validated_chapters.append(f"{timestamp_str} {title}")
            continue
        
        context = ' '.join(context_texts[:50])  # Limit context to avoid token overflow
        
        # Ask AI if the timestamp matches the description
        validation_prompt = f"""
        You are validating a chapter marker for a video transcript.
        
        Chapter description: "{title}"
        Current timestamp: {timestamp_str}
        
        Here's what is actually being said around {timestamp_str}:
        "{context}"
        
        Does this text match the chapter description "{title}"?
        
        Respond with ONLY one of these:
        VALID - if the description matches what's being said at this time
        INVALID - if the description does NOT match what's being said at this time
        """
        
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": validation_prompt}
                ],
                temperature=0.2,
                max_tokens=20
            )
            
            result = response.choices[0].message.content.strip().upper()
            
            if "VALID" in result and "INVALID" not in result:
                # Keep original timestamp
                validated_chapters.append(f"{timestamp_str} {title}")
                print(f"  ✓ {timestamp_str} - Timestamp validated for '{title}'")
            else:
                # Need to find the correct timestamp for this description
                print(f"  🔍 {timestamp_str} - Searching for correct timestamp for '{title}'...")
                
                # Find the next chapter's timestamp to ensure we don't go past it
                next_chapter_seconds = None
                current_idx = parsed.index((seconds, timestamp_str, title))
                if current_idx < len(parsed) - 1:
                    next_chapter_seconds = parsed[current_idx + 1][0]
                
                # Search through the transcript to find where this topic is discussed
                correct_timestamp = find_correct_timestamp(title, all_segments, time_to_text, client, seconds, next_chapter_seconds)
                
                if correct_timestamp and correct_timestamp != timestamp_str:
                    validated_chapters.append(f"{correct_timestamp} {title}")
                    print(f"  ✏ Timestamp corrected: {timestamp_str} → {correct_timestamp}")
                else:
                    # Keep original if we couldn't find a better match
                    validated_chapters.append(f"{timestamp_str} {title}")
                    print(f"  ⚠ Could not find better timestamp, keeping {timestamp_str}")
                
        except Exception as e:
            print(f"  ! {timestamp_str} - Validation error: {str(e)}, keeping original")
            validated_chapters.append(f"{timestamp_str} {title}")
    
    return '\n'.join(validated_chapters)

def find_correct_timestamp(description, all_segments, time_to_text, client, original_seconds, next_chapter_seconds=None):
    """
    Search through the transcript to find where a topic is actually discussed.
    Only searches within ±60 seconds of the original timestamp.
    @param description: The chapter description to find
    @param all_segments: List of (timestamp, text) tuples
    @param time_to_text: Dict mapping timestamps to text
    @param client: OpenAI client
    @param original_seconds: The original timestamp in seconds
    @param next_chapter_seconds: Timestamp of next chapter (don't search past this)
    @return: Corrected timestamp string or None
    """
    # Define search window: ±60 seconds from original
    search_window = 60
    min_time = max(0, original_seconds - search_window)
    max_time = original_seconds + search_window
    
    # Don't search past the next chapter
    if next_chapter_seconds is not None:
        max_time = min(max_time, next_chapter_seconds - 5)  # Stay 5 seconds before next chapter
    
    # Create text windows every 10 seconds within the search range
    windows = []
    current_time = min_time
    
    while current_time <= max_time:
        window_texts = []
        for time_sec in range(current_time, min(current_time + 10, max_time + 1)):
            if time_sec in time_to_text:
                window_texts.extend(time_to_text[time_sec])
        
        if window_texts:
            windows.append((current_time, ' '.join(window_texts[:30])))  # Limit text per window
        
        current_time += 10
    
    if not windows:
        return None
    
    # Build a prompt with the windows
    windows_text = "\n\n".join([f"[{format_duration(w[0])}]: {w[1][:200]}" for w in windows])
    
    search_prompt = f"""
    You are fine-tuning a chapter timestamp for a video transcript.
    
    Topic: "{description}"
    Original timestamp: {format_duration(original_seconds)}
    
    Here is text from within ±60 seconds of that timestamp:
    
    {windows_text}
    
    Which timestamp is the BEST match for when "{description}" begins?
    The timestamp should be close to {format_duration(original_seconds)}.
    
    Respond with ONLY the timestamp in HH:MM:SS format (e.g., 00:05:17).
    If the original timestamp is already good, respond with: {format_duration(original_seconds)}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": search_prompt}
            ],
            temperature=0.2,
            max_tokens=20
        )
        
        result = response.choices[0].message.content.strip()
        
        # Check if result is a valid timestamp
        if ":" in result:
            # Validate it's in HH:MM:SS format
            import re
            if re.match(r'^\d{1,2}:\d{2}:\d{2}$', result):
                # Make sure the result is within our search window
                result_seconds = parse_timestamp_to_seconds(result)
                if min_time <= result_seconds <= max_time:
                    return result
                else:
                    print(f"    Timestamp {result} outside search window, keeping original")
                    return None
        
        return None
        
    except Exception as e:
        print(f"    Error searching for timestamp: {str(e)}")
        return None

def create_chapters(transcript, video_id, raw_transcript=None, summary=None):
    """
    Create timestamps and chapters for a YouTube video transcript.
    @param transcript: The raw transcript of a YouTube video
    @param video_id: The YouTube video ID
    @param raw_transcript: Raw transcript data with timing information (optional)
    @param summary: Summary of the video content (optional)
    @return: A string containing formatted timestamps and chapters
    """
    if openai_key == "":
        print("No OpenAI API key found in .env file; skipping chapter creation.")
        return "Chapters not available"

    client = openai.OpenAI(api_key=openai_key)
    
    # Get video duration if available
    duration_seconds = get_video_duration(raw_transcript) if raw_transcript else None
    duration_constraint = ""
    if duration_seconds:
        duration_str = format_duration(duration_seconds)
        duration_constraint = f"\n\nIMPORTANT: This video is {duration_str} long. DO NOT generate any timestamps beyond {duration_str}. All timestamps must be less than or equal to {duration_str}."

    # Build a timeline skeleton from raw transcript if available
    timeline_context = ""
    if raw_transcript:
        print(f"Building timeline skeleton from raw transcript for video {video_id} (duration: {format_duration(duration_seconds) if duration_seconds else 'unknown'})")
        
        # Build mapping of time to text (reusing existing logic)
        time_to_texts = {}
        for entry in raw_transcript:
            if isinstance(entry, dict) and 'text' in entry and 'start' in entry:
                text = entry['text'].strip()
                if text and text not in ['[Music]', '[Applause]', '[Laughter]']:
                    start_time = int(entry['start'])
                    if start_time not in time_to_texts:
                        time_to_texts[start_time] = []
                    time_to_texts[start_time].append(text)
        
        # Create timeline samples dynamically based on video duration
        timeline_samples = []
        video_duration = duration_seconds or 3600
        
        # Dynamically adjust sample interval based on video length
        # Target ~50-60 samples total to cover the entire video while staying within token limits
        target_samples = 55
        sample_interval = max(15, video_duration // target_samples)  # At least 15 seconds between samples
        
        current_time = 0
        sample_count = 0
        
        while current_time <= video_duration and sample_count < target_samples:
            # Get text from a small window around this time
            window_texts = []
            for time_sec in range(current_time, min(current_time + 10, video_duration + 1)):
                if time_sec in time_to_texts:
                    window_texts.extend(time_to_texts[time_sec])
            
            if window_texts:
                # Take first few words as a sample
                sample_text = ' '.join(window_texts)[:150]  # Limit length
                timestamp_str = format_duration(current_time)
                timeline_samples.append(f"[{timestamp_str}]: {sample_text}")
                sample_count += 1
            
            current_time += sample_interval
        
        if timeline_samples:
            print(f"  Created {len(timeline_samples)} timeline samples (interval: ~{sample_interval}s) covering entire video")
            timeline_context = f"""

TIMELINE REFERENCE - These are actual timestamps from the video showing what is being said at different times (covering the ENTIRE {format_duration(video_duration)} video):

{chr(10).join(timeline_samples)}

USE THESE ACTUAL TIMESTAMPS to determine when topics change. Review the ENTIRE timeline above before selecting chapters. Your chapter timestamps MUST come from the times shown above or nearby times. DO NOT guess or make up timestamps."""
    
    # Include summary context if available
    summary_context = ""
    if summary:
        summary_context = f"""

VIDEO SUMMARY - Use this to understand what topics and people are actually important in this video:

{summary}

IMPORTANT: Create chapters ONLY for the topics, people, and discussions mentioned in the summary above. If something isn't in the summary (like casual small talk about weather), it's not important enough for a chapter."""

    chapters_prompt = f"""
    This is a transcript of a YouTube livestream. 
    
    TASK: Read through the ENTIRE video (see timeline reference below) and identify the 10 MOST IMPORTANT moments to create chapters for, in this format:
    00:00:00 Introductions 
    00:01:47 What is structured metadata?
    00:03:22 Discussion about metrics
    00:05:30 Guest introduction: Diana
    
    IMPORTANT: Review the timeline reference showing the ENTIRE video before deciding on chapters. Distribute chapters across the full video length, not just the beginning.

    WHAT MAKES A GOOD CHAPTER:
    - Topics and people mentioned in the VIDEO SUMMARY above
    - Guest introductions (when new people join the conversation)
    - Major topic changes (switching from one main subject to another)
    - Substantive discussions, demos, or explanations that align with the summary
    - Q&A sessions or audience interactions
    - Significant announcements or reveals
    
    DO NOT CREATE CHAPTERS FOR:
    - Anything NOT mentioned in the VIDEO SUMMARY (if summary is provided)
    - Brief small talk, pleasantries, or casual mentions (weather, travel, casual greetings)
    - Filler conversation or off-topic tangents
    - Single sentences or passing comments about unrelated topics
    - Technical difficulties, pauses, or transitions
    - Topics that last less than 30 seconds
    
    DECISION PROCESS:
    1. Read through the ENTIRE timeline reference to understand the full video
    2. Identify all significant moments that match topics in the VIDEO SUMMARY
    3. Select the 10 MOST IMPORTANT moments distributed across the entire video
    4. For each moment: check if the topic/person is mentioned in the VIDEO SUMMARY
    5. If YES and it's a significant moment → include as a chapter
    6. If NO or it's just small talk → skip it
    
    FOCUS ON: What would viewers actually want to jump to? What are the main topics identified in the summary? Make sure to cover the ENTIRE video, not just the beginning.

    CRITICAL INSTRUCTIONS:
    - Always start with 00:00:00 (typically "Introductions" or "Welcome")
    - Use the ACTUAL timestamps from the timeline reference below
    - DO NOT round timestamps to neat intervals like :00 or :30
    - Use precise timestamps like 00:05:17, 00:12:43, 00:08:09, etc.
    - Look at the actual flow of conversation to determine when MAJOR topics change
    - The chapter description MUST accurately describe what is being said RIGHT AT that timestamp
    - Do NOT describe what happens later - only describe what is happening at the exact moment of the timestamp
    - Read the timeline reference carefully to see what's actually being said at each time
    - If a guest is introduced at 00:05:30, don't put "Guest introduction" at 00:20:00
    - Be precise and honest about what's happening at each moment
    - KEEP DESCRIPTIONS CONCISE: Use 2-6 words maximum, not full sentences
    - Descriptions should be SHORT PHRASES like "Guest introduction", "Discussion about X", "Demo of Y feature"
    - DO NOT write full sentences or lengthy explanations in the chapter titles{duration_constraint}{summary_context}{timeline_context}
    """

    print(f"Creating chapters for video {video_id}")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": chapters_prompt},
            {"role": "user", "content": transcript}
        ],
        temperature=0.3,  # Lower temperature for more accurate, less creative responses
    )

    chapters = response.choices[0].message.content
    # Clean any AI preamble before returning
    chapters = clean_ai_preamble(chapters)
    
    # Validate and fix chapter descriptions
    if raw_transcript:
        chapters = validate_and_fix_chapters(chapters, raw_transcript, video_id)
    
    return chapters

def write_markdown(args, video):
    video_id = get_id(video)
    
    if video_id == '':
        print(f"Could not write markdown for video")
        print(json.dumps(video, indent=2))
        return 

    published = get_publish(video)
    title = video['snippet']['title']
    description = video['snippet']['description']
    transcript = video.get('transcript', '')
    raw_transcript = video.get('raw_transcript', [])

    if transcript == '':
        print(f"Skipping video {video_id} / {title} because it has no transcript.")
        return 

    url = f"https://www.youtube.com/watch?v={video_id}"

    filename = file_for_video(args, video)
    [summary, cleaned_up] = openai_cleanup(transcript, video_id)
    chapters = create_chapters(transcript, video_id, raw_transcript, summary)
    
    # Parse chapters and insert timestamps into cleaned transcript
    parsed_chapters = parse_chapters(chapters)
    if cleaned_up and parsed_chapters and raw_transcript:
        cleaned_up = insert_timestamps_in_transcript(cleaned_up, parsed_chapters, raw_transcript)

    with open(filename, "w") as file:
        file.write(f"# {title}\n\n")
        file.write(f"Published on {published}\n\n")
        file.write(f"## Description\n\n{description}\n\n")
        file.write(f"URL: {url}\n\n")
    
        file.write("## Summary\n\n") 
        file.write(f"{summary}\n\n")
        
        file.write("## Chapters\n\n")
        file.write(f"{chapters}\n\n")
        
        if cleaned_up:
            file.write("## Transcript\n\n")
            file.write(f"{cleaned_up}\n\n")

        # TODO: if we're happy with OpenAI output, this is extraneous and can go.
        # The YouTube transcripts are uhm ah well excessively uhm ah accurate.
        file.write("## Raw YouTube Transcript\n\n")
        file.write(f"{transcript}\n\n")

    print(f"Successfully wrote transcript for video {video_id} to {filename}")

def have_transcript_file(args, video):
    return os.path.isfile(file_for_video(args, video))

def main(args):
    videos_to_transcribe = []

    if args.playlist:
        print("Fetching playlist videos")
        playlist_videos = get_playlist_videos(args.playlist)
        videos_to_transcribe = videos_to_transcribe + playlist_videos
        print(f"Found {len(playlist_videos)} videos in playlist %s" % args.playlist)

    if args.channel:
        print("Fetching channel videos")
        channel_videos = get_channel_videos(args.channel, args.start, args.end)
        videos_to_transcribe = videos_to_transcribe + channel_videos
        print(f"Found {len(channel_videos)} videos in the specified date range.")

    videos_to_transcribe = [v for v in videos_to_transcribe if not have_transcript_file(args, v)]
    print(f"Found {len(videos_to_transcribe)} videos to transcribe, after filtering out those that already have transcripts.")

    if args.limit:
        videos_to_transcribe = videos_to_transcribe[:args.limit]
        print(f"Limiting to {args.limit} videos.")

    videos = fetch_transcripts(args, videos_to_transcribe)
    print("Done")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog='transcripts',
            description='Extracts Transcripts from YouTube and writes them as local markdown files')
    parser.add_argument('-c', '--channel', required=False,
                        help='YouTube Channel ID; defaults to OpenTelemetry', 
                        default='UCHZDBZTIfdy94xMjMKz-_MA')
    parser.add_argument('-p', '--playlist', required=False,
                        help='YouTube Playlist ID; no default.',
                        default=None)
    parser.add_argument('-s', '--start', required=False,
                        help='Start date for videos; Must be in ISO 8601 format. defaults to 2024-01-01T00:00:00Z',
                        default='2023-01-01T00:00:00Z')
    parser.add_argument('-e', '--end', required=False,
                        help='End date for videos; Must be in ISO 8601 format. defaults to 2030-12-31T00:00:00Z to get all',
                        default='2030-12-31T00:00:00Z')
    parser.add_argument('-d', '--path', 
                        help='Path to write markdown files to; defaults to current directory',
                        required=False, default='./transcripts/')
    parser.add_argument('-l', '--limit', 
                        help='Limit the number of videos to transcribe; defaults to no limit',
                        required=False, default=None, type=int)
    args = parser.parse_args()

    main(args)
