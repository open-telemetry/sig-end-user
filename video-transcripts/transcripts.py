import os
import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
from youtube_transcript_api._errors import YouTubeRequestFailed
try:
    from youtube_transcript_api._errors import TooManyRequests
except ImportError:
    # Fallback if TooManyRequests doesn't exist in this version
    TooManyRequests = YouTubeRequestFailed
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

def get_playlist_videos(playlist_id):
    youtube = build('youtube', 'v3', developerKey=youtube_key)
    
    video_ids = []
    next_page_token = None

    # This returns a list of youtube:playlistItem with rate limiting
    while True:
        try:
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
                
            # Small delay between pagination requests
            delay = random.uniform(1, 3)  # Random delay between 1-3 seconds
            print(f"Waiting {delay:.1f} seconds before next page...")
            time.sleep(delay)
            
        except HttpError as e:
            if e.resp.status == 403 and 'quota' in str(e).lower():
                print("Quota exceeded while fetching playlist items. Waiting before retry...")
                time.sleep(60)  # Wait 1 minute
                continue
            else:
                print(f"Error fetching playlist items: {e}")
                raise

    # Fetch video details in batches with rate limiting
    videos = []
    batch_size = 50  # YouTube API allows up to 50 IDs per request
    
    for i in range(0, len(video_ids), batch_size):
        batch_ids = video_ids[i:i + batch_size]
        
        try:
            request = youtube.videos().list(
                part='snippet',
                id=','.join(batch_ids)
            )
            response = request.execute()
            
            for item in response['items']:
                print(f"Found video: {item['snippet']['title']}")
                videos.append(item)
                
            # Rate limiting between batches
            time.sleep(0.2)  # 200ms delay between batches
            
        except HttpError as e:
            if e.resp.status == 403 and 'quota' in str(e).lower():
                print(f"Quota exceeded on video details batch {i//batch_size + 1}. Waiting before retry...")
                time.sleep(60)
                continue
            else:
                print(f"Error fetching video details batch {i//batch_size + 1}: {e}")
                continue

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
                
            # Small delay between pagination requests
            delay = random.uniform(1, 3)  # Random delay between 1-3 seconds
            print(f"Waiting {delay:.1f} seconds before next page...")
            time.sleep(delay)
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
        transcript_text = get_video_transcript_with_retry(video_id)
        
        if transcript_text:
            video['transcript'] = transcript_text
            processed.append(video)
            write_markdown(args, video)
        else:
            print(f"Skipping video {video_id} due to transcript issues.")
            
        # Small delay between transcript fetches
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
    Returns cleaned transcript text or None if unavailable.
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
                return None
                
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
                return None
                
            full_text = ' '.join(text_parts)
            
            # Minimum length validation
            if len(full_text.strip()) < 50:
                print(f"Transcript too short for video {video_id}: {len(full_text)} characters")
                return None
                
            return full_text
            
        except TranscriptsDisabled:
            print(f"Transcripts are disabled for video {video_id}")
            return None
        except NoTranscriptFound:
            print(f"No transcript found for video {video_id}")
            return None
        except VideoUnavailable:
            print(f"Video {video_id} is unavailable")
            return None
        except YouTubeRequestFailed as e:
            # Check if this is an IP block error
            error_str = str(e)
            if 'blocking requests from your IP' in error_str or 'IP has been blocked' in error_str:
                print(f"❌ YouTube has blocked your IP address for video {video_id}")
                print(f"   This is not a temporary rate limit - your IP is blocked.")
                print(f"\n   Workarounds:")
                print(f"   1. Wait 24-48 hours for the block to clear")
                print(f"   2. Use a different network/WiFi connection")
                print(f"   3. Set up cookie-based authentication (see README)")
                print(f"   4. Use a residential proxy or VPN (not cloud-based)")
                return None
            elif '429' in error_str or 'Too Many Requests' in error_str:
                if attempt < max_retries - 1:
                    # Use much longer wait time for rate limiting (60-120 seconds)
                    wait_time = random.uniform(60, 120)
                    print(f"⚠️  YouTube rate limit (429) detected for video {video_id}")
                    print(f"   Waiting {wait_time:.0f} seconds before retry {attempt + 2}/{max_retries}...")
                    time.sleep(wait_time)
                else:
                    print(f"❌ YouTube rate limit persists after {max_retries} attempts for video {video_id}")
                    print(f"   Consider waiting 10-15 minutes before running the script again.")
                    return None
            else:
                # Other YouTube API errors
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt) * 5 + random.uniform(0, 5)
                    print(f"YouTube API error for video {video_id}. Retrying in {wait_time:.1f}s...")
                    time.sleep(wait_time)
                else:
                    print(f"YouTube API error persists for video {video_id}: {str(e)}")
                    return None
        except Exception as e:
            error_str = str(e)
            # Check if this is likely a rate limit error disguised as XML parse error
            if 'no element found' in error_str or 'line 1, column 0' in error_str:
                if attempt < max_retries - 1:
                    # Use longer wait time as this is likely a rate limit issue
                    wait_time = random.uniform(60, 120)
                    print(f"⚠️  Possible YouTube rate limit detected for video {video_id} (XML parse error)")
                    print(f"   Waiting {wait_time:.0f} seconds before retry {attempt + 2}/{max_retries}...")
                    time.sleep(wait_time)
                else:
                    print(f"❌ Persistent error for video {video_id} after {max_retries} attempts")
                    print(f"   This may be due to YouTube rate limiting. Wait 10-15 minutes and try again.")
                    return None
            elif attempt < max_retries - 1:
                # Standard exponential backoff for other errors
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                print(f"Attempt {attempt + 1} failed for video {video_id}. Retrying in {wait_time:.1f}s... Error: {error_str}")
                time.sleep(wait_time)
            else:
                print(f"All {max_retries} attempts failed for video {video_id}: {error_str}")
                return None
    
    return None

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

    Please output your results as markdown text; you may use markdown formatting for emphasis, bold,
    bulleting, and so on. 

    Stay as close to the original transcript as possible but make it more readable. Do not interpret,
    add, or remove any words unless they are filler words.  
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

def create_chapters(transcript, video_id):
    """
    Create timestamps and chapters for a YouTube video transcript.
    @param transcript: The raw transcript of a YouTube video
    @param video_id: The YouTube video ID
    @return: A string containing formatted timestamps and chapters
    """
    if openai_key == "":
        print("No OpenAI API key found in .env file; skipping chapter creation.")
        return "Chapters not available"

    client = openai.OpenAI(api_key=openai_key)

    chapters_prompt = """
    This is a transcript of a YouTube livestream. Could you please identify up to 10 key moments in the stream and give me the timestamps in the format for YouTube like this?: 
    00:00:00 Introductions 
    00:01:30 What is structured metadata?

    Always start with 00:00:00 and use simple but descriptive language that makes it easier for users to understand what is being spoken about.
    """

    print(f"Creating chapters for video {video_id}")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": chapters_prompt},
            {"role": "user", "content": transcript}
        ],
        temperature=0.7,
    )

    chapters = response.choices[0].message.content
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

    if transcript == '':
        print(f"Skipping video {video_id} / {title} because it has no transcript.")
        return 

    url = f"https://www.youtube.com/watch?v={video_id}"

    filename = file_for_video(args, video)
    [summary, cleaned_up] = openai_cleanup(transcript, video_id)
    chapters = create_chapters(transcript, video_id)

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
            # Don't write a heading because OpenAI was instructed to output markdown.
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
        
        # Small delay between different API calls
        if args.channel:
            delay = random.uniform(2, 4)
            print(f"Waiting {delay:.1f} seconds before fetching channel videos...")
            time.sleep(delay)

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
