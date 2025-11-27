# YouTube Transcripts

This directory contains a small script which fetches transcripts from the YouTube API, so that we can 
keep text/markdown corresponding to the transcripts of the videos that the community produces.

## Setup

* `python3 -m venv venv`
* `source venv/bin/activate`
* `pip3 install -r requirements.txt`

## Dependency Management

This project uses `pip-tools` to manage dependencies:

* **Direct dependencies** are listed in `requirements.in`
* **All dependencies** (direct + transitive) are locked in `requirements.txt`

### Updating Dependencies

To add or update a direct dependency:

1. Edit `requirements.in` to add/modify the dependency
2. Install `pip-tools` if not already installed: `pip install pip-tools`
3. Regenerate `requirements.txt`: `pip-compile requirements.in -o requirements.txt`
4. Install updated dependencies: `pip install -r requirements.txt`

**Note:** Renovate is configured to only update `requirements.in`. Do not manually edit `requirements.txt`.

## Running Tests

To run the unit tests:

```bash
python -m unittest test_transcripts.py -v
```

## Configure Environment

Edit `.env` file and set `API_KEY` to the correct value for YouTube
Optionally, add `OPENAI_API_KEY` if you intend to use the categorizer

## Run & Pull Transcripts!

Typical usage will involve a YouTube Channel ID, which is in the [URL for the channel](https://www.youtube.com/channel/UCHZDBZTIfdy94xMjMKz-_MA)

From within this directory, we'd place transcripts in that directory off of the root.

```
python3 transcripts.py \
    --channel UCHZDBZTIfdy94xMjMKz-_MA \
    --path ./transcripts
```

## Need a YouTube Key?

* Have a GCP project
* Go to a GCP project, make sure YouTube Data API v3 is enabled
* Create an API key in that project and use that for this value.

