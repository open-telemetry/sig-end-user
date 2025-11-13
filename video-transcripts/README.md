# YouTube Transcripts

This directory contains a script that fetches transcripts from YouTube videos and generates markdown files with:
- Video metadata (title, description, publish date)
- AI-generated summary of the content
- Chapters/timestamps for easy navigation
- Cleaned up transcript with proper formatting
- Raw YouTube transcript for reference

## Setup

* `python3 -m venv venv`
* `source venv/bin/activate`
* `pip3 install -r requirements.txt`

## Configure Environment

Edit `.env` file and set `API_KEY` to the correct value for YouTube
Optionally, add `OPENAI_API_KEY` if you intend to use the categorizer

- **`API_KEY`** (required): YouTube Data API v3 key for fetching video data and transcripts
- **`OPENAI_API_KEY`** (optional): OpenAI API key for AI-enhanced features:
  - Generates concise summaries of video content
  - Creates YouTube-style chapter timestamps (e.g., `00:00:00 Introduction`)
  - Cleans up raw transcripts into readable markdown format

If `OPENAI_API_KEY` is not provided, the script will still fetch and save raw transcripts, but summaries and chapters will be unavailable.

## Usage

### Basic Usage - Channel

Fetch transcripts from a YouTube channel (defaults to OpenTelemetry channel):

```bash
python3 transcripts.py --channel UCHZDBZTIfdy94xMjMKz-_MA --path ./transcripts
```

### Fetch from Playlist

```bash
python3 transcripts.py --playlist PLDGkOdUX1UjrEOz4fOB4UZW8m-hx8_mtb --path ./transcripts
```

### Command-Line Options

- `-c, --channel`: YouTube Channel ID (default: OpenTelemetry channel)
- `-p, --playlist`: YouTube Playlist ID (no default)
- `-s, --start`: Start date for videos in ISO 8601 format (default: `2023-01-01T00:00:00Z`)
- `-e, --end`: End date for videos in ISO 8601 format (default: `2030-12-31T00:00:00Z`)
- `-d, --path`: Directory to write markdown files to (default: `./transcripts/`)
- `-l, --limit`: Limit the number of videos to process (useful for testing)

### Example with Date Range and Limit

```bash
python3 transcripts.py \
    --channel UCHZDBZTIfdy94xMjMKz-_MA \
    --start 2024-01-01T00:00:00Z \
    --end 2024-12-31T00:00:00Z \
    --limit 5 \
    --path ./transcripts
```

## Output Format

Each video generates a markdown file named: `{publish_date}-{slugified-title}.md`

The generated markdown includes:
- **Title and Metadata**: Video title, publish date, description, and YouTube URL
- **Summary**: AI-generated one-paragraph overview of the video content
- **Chapters**: YouTube-style timestamps identifying key moments (e.g., `00:00:00 Introduction`)
- **Cleaned Transcript**: Readable, formatted transcript with proper paragraphs
- **Raw Transcript**: Original YouTube auto-generated transcript for reference

## Features & Reliability

### Rate Limiting
The script includes comprehensive rate limiting to avoid YouTube API quota issues:
- Random delays between API requests (3-8 seconds for pagination)
- Longer delays between video processing (10-30 seconds)
- Initial startup delay to "cool down" the API
- Automatic 60-second wait and retry when quota limits are hit

### Error Handling
- Exponential backoff with up to 3 retry attempts for transcript fetching
- Graceful handling of videos with disabled transcripts
- Validates transcript quality (minimum length, filters music/applause markers)
- Skips videos that already have transcripts (resumes interrupted runs)

### Language Support
Attempts to fetch transcripts in multiple languages: English, Spanish, French, German, Japanese

## Need a YouTube Key?

* Have a GCP project
* Go to a GCP project, make sure YouTube Data API v3 is enabled
* Create an API key in that project and use that for this value.

