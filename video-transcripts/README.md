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

Copy the example environment file and configure your API keys:

```bash
cp env.example .env
```

Edit `.env` file and set `API_KEY` to the correct value for YouTube.
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
- Small delays between video transcript fetches (2-5 seconds) to prevent rate limiting
- Automatic 60-120 second wait and retry when rate limits (429 errors) are hit
- Exponential backoff for transient errors
- Detects and reports IP blocking vs. temporary rate limiting

### Error Handling
- Exponential backoff with up to 3 retry attempts for transcript fetching
- Graceful handling of videos with disabled transcripts
- Validates transcript quality (minimum length, filters music/applause markers)
- Skips videos that already have transcripts (resumes interrupted runs)

### Language Support
Attempts to fetch transcripts in multiple languages: English, Spanish, French, German, Japanese

## Troubleshooting

### YouTube IP Blocking

If you encounter "YouTube is blocking requests from your IP" errors, this means YouTube has blocked your IP address from accessing their transcript API. This is different from rate limiting and won't clear quickly.

**Common causes:**
- Repeated testing/debugging over multiple days
- Using a cloud provider IP (AWS, GCP, Azure, etc.)
- Using certain VPN services
- Your ISP's IP range being flagged

**Solutions:**

1. **Wait 24-48 hours** - IP blocks usually clear after 1-2 days of no activity

2. **Use a different network** - Switch to mobile hotspot, different WiFi, or different location

3. **Cookie-based authentication** (Advanced):
   - Export cookies from a logged-in YouTube session in your browser
   - Use a browser extension like "Get cookies.txt LOCALLY" (Chrome/Firefox)
   - Save cookies.txt in the video-transcripts directory
   - Modify the script to use cookies (requires code changes)
   - See [youtube-transcript-api documentation](https://github.com/jdepoix/youtube-transcript-api#cookies) for details

4. **Use a residential proxy** - Cloud/datacenter IPs are often blocked, but residential IPs work better

5. **Run from a different machine** - If possible, run the script from a home computer instead of a server

## Need a YouTube Key?

* Have a GCP project
* Go to a GCP project, make sure YouTube Data API v3 is enabled
* Create an API key in that project and use that for this value.

