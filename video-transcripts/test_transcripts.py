import unittest
import os
import tempfile
from argparse import Namespace
from unittest.mock import patch, MagicMock
from transcripts import (
    get_publish,
    get_id,
    file_for_video,
    have_transcript_file,
    get_playlist_videos,
    get_channel_videos,
    fetch_transcripts,
    openai_cleanup
)


class TestTranscripts(unittest.TestCase):
    """Unit tests for the transcripts.py script"""

    def setUp(self):
        """Set up test fixtures"""
        # Create a temporary directory for test outputs
        self.temp_dir_obj = tempfile.TemporaryDirectory()
        self.test_dir = self.temp_dir_obj.name

        # Sample video data from YouTube API response (playlist video format)
        self.playlist_video = {
            'id': 'ABC123xyz',
            'snippet': {
                'title': 'Test Video Title',
                'description': 'Test description',
                'publishedAt': '2024-01-15T10:30:00Z'
            }
        }

        # Sample video data from YouTube API response (search result format)
        self.search_video = {
            'id': {
                'videoId': 'XYZ789abc'
            },
            'snippet': {
                'title': 'Search Result Video',
                'description': 'Search result description',
                'publishTime': '2024-02-20T14:45:00Z',
                'publishedAt': '2024-02-20T14:45:00Z'
            }
        }

    def tearDown(self):
        """Clean up test fixtures"""
        # Cleanup happens automatically when TemporaryDirectory context exits
        self.temp_dir_obj.cleanup()

    def test_get_publish_with_publish_time(self):
        """Test get_publish returns publishTime when available"""
        result = get_publish(self.search_video)
        self.assertEqual(result, '2024-02-20T14:45:00Z')

    def test_get_publish_with_published_at(self):
        """Test get_publish falls back to publishedAt when publishTime is not available"""
        result = get_publish(self.playlist_video)
        self.assertEqual(result, '2024-01-15T10:30:00Z')

    def test_get_id_with_string(self):
        """Test get_id when id is a string (playlist format)"""
        result = get_id(self.playlist_video)
        self.assertEqual(result, 'ABC123xyz')

    def test_get_id_with_dict(self):
        """Test get_id when id is a dict (search result format)"""
        result = get_id(self.search_video)
        self.assertEqual(result, 'XYZ789abc')

    def test_file_for_video_creates_correct_filename(self):
        """Test file_for_video generates a properly slugified filename"""
        args = Namespace(path=self.test_dir)
        result = file_for_video(args, self.playlist_video)

        expected = f"{self.test_dir}/2024-01-15T10:30:00Z-test-video-title.md"
        self.assertEqual(result, expected)

    def test_file_for_video_with_special_characters(self):
        """Test file_for_video properly slugifies special characters"""
        video_with_special_chars = {
            'id': 'TEST123',
            'snippet': {
                'title': 'Test: Video! With @Special #Characters',
                'publishedAt': '2024-03-01T12:00:00Z'
            }
        }
        args = Namespace(path=self.test_dir)
        result = file_for_video(args, video_with_special_chars)

        # Slug should remove or convert special characters in the title portion
        slug_part = result.split('/')[-1].split('Z-')[-1]  # Get the slug part after timestamp
        self.assertIn('test-video-with-special-characters', slug_part)
        self.assertNotIn('!', slug_part)
        self.assertNotIn('@', slug_part)
        self.assertNotIn('#', slug_part)

    def test_file_for_video_missing_publish_time_raises_exception(self):
        """Test file_for_video raises exception when publish time is missing"""
        video_without_publish = {
            'id': 'TEST123',
            'snippet': {
                'title': 'Test Video'
            }
        }
        args = Namespace(path=self.test_dir)

        # Should raise KeyError when publishedAt or publishTime is missing
        with self.assertRaises(KeyError):
            file_for_video(args, video_without_publish)

    def test_have_transcript_file_returns_false_when_file_does_not_exist(self):
        """Test have_transcript_file returns False when file doesn't exist"""
        args = Namespace(path=self.test_dir)
        result = have_transcript_file(args, self.playlist_video)
        self.assertFalse(result)

    def test_have_transcript_file_returns_true_when_file_exists(self):
        """Test have_transcript_file returns True when file exists"""
        args = Namespace(path=self.test_dir)

        # Create the file that would be generated
        filename = file_for_video(args, self.playlist_video)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as f:
            f.write('Test content')

        result = have_transcript_file(args, self.playlist_video)
        self.assertTrue(result)

    @patch('transcripts.build')
    def test_get_playlist_videos_integration(self, mock_build):
        """Test get_playlist_videos with mocked YouTube API"""
        # Mock YouTube API responses
        mock_youtube = MagicMock()
        mock_build.return_value = mock_youtube

        # Mock playlistItems().list() response
        mock_playlist_response = {
            'items': [
                {'snippet': {'resourceId': {'videoId': 'video1'}}},
                {'snippet': {'resourceId': {'videoId': 'video2'}}}
            ]
        }
        mock_youtube.playlistItems().list().execute.return_value = mock_playlist_response

        # Mock videos().list() response
        mock_videos_response = {
            'items': [
                {
                    'id': 'video1',
                    'snippet': {
                        'title': 'Test Video 1',
                        'description': 'Description 1',
                        'publishedAt': '2024-01-01T00:00:00Z'
                    }
                },
                {
                    'id': 'video2',
                    'snippet': {
                        'title': 'Test Video 2',
                        'description': 'Description 2',
                        'publishedAt': '2024-01-02T00:00:00Z'
                    }
                }
            ]
        }
        mock_youtube.videos().list().execute.return_value = mock_videos_response

        # Call the function
        result = get_playlist_videos('test_playlist_id')

        # Verify results
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['id'], 'video1')
        self.assertEqual(result[0]['snippet']['title'], 'Test Video 1')
        self.assertEqual(result[1]['id'], 'video2')

        # Verify API was called correctly
        mock_build.assert_called_once()
        mock_youtube.playlistItems().list.assert_called()
        mock_youtube.videos().list.assert_called()

    @patch('transcripts.build')
    def test_get_channel_videos_integration(self, mock_build):
        """Test get_channel_videos with mocked YouTube API"""
        # Mock YouTube API
        mock_youtube = MagicMock()
        mock_build.return_value = mock_youtube

        # Mock search().list() response
        mock_search_response = {
            'items': [
                {
                    'id': {'videoId': 'channel_video1'},
                    'snippet': {
                        'title': 'Channel Video 1',
                        'publishedAt': '2024-01-15T00:00:00Z'
                    }
                }
            ]
        }
        mock_youtube.search().list().execute.return_value = mock_search_response

        # Call the function
        result = get_channel_videos('test_channel', '2024-01-01T00:00:00Z', '2024-12-31T00:00:00Z')

        # Verify results
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id']['videoId'], 'channel_video1')
        self.assertEqual(result[0]['snippet']['title'], 'Channel Video 1')

        # Verify API was called correctly
        mock_build.assert_called_once()
        mock_youtube.search().list.assert_called()

    @patch('transcripts.YouTubeTranscriptApi')
    @patch('transcripts.openai_cleanup')
    def test_fetch_transcripts_integration(self, mock_cleanup, mock_transcript_api):
        """Test fetch_transcripts with mocked APIs"""
        # Mock transcript API
        mock_transcript = [
            {'text': 'Hello', 'start': 0.0},
            {'text': 'World', 'start': 1.0}
        ]
        mock_transcript_api.get_transcript.return_value = mock_transcript

        # Mock OpenAI cleanup
        mock_cleanup.return_value = ['Test summary', 'Cleaned transcript']

        # Create test video
        test_video = {
            'id': 'test123',
            'snippet': {
                'title': 'Test Video',
                'description': 'Test description',
                'publishedAt': '2024-01-01T00:00:00Z'
            }
        }

        args = Namespace(path=self.test_dir)

        # Call the function
        result = fetch_transcripts(args, [test_video])

        # Verify transcript was fetched
        mock_transcript_api.get_transcript.assert_called_once_with(
            'test123',
            languages=('en', 'es', 'fr', 'de', 'jp')
        )

        # Verify the video has transcript
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['transcript'], 'Hello World')

        # Verify file was created
        expected_file = f"{self.test_dir}/2024-01-01T00:00:00Z-test-video.md"
        self.assertTrue(os.path.exists(expected_file))

        # Verify file contents
        with open(expected_file, 'r') as f:
            content = f.read()
            self.assertIn('# Test Video', content)
            self.assertIn('Test summary', content)
            self.assertIn('Hello World', content)

    @patch('transcripts.openai.OpenAI')
    @patch('transcripts.openai_key', 'test_api_key')
    def test_openai_cleanup_integration(self, mock_openai_class):
        """Test openai_cleanup with mocked OpenAI client"""
        # Mock OpenAI client and responses
        mock_client = MagicMock()
        mock_openai_class.return_value = mock_client

        # Mock the chat completion responses
        mock_summary_response = MagicMock()
        mock_summary_response.choices = [MagicMock()]
        mock_summary_response.choices[0].message.content = "This is a test summary of the video."

        mock_cleanup_response = MagicMock()
        mock_cleanup_response.choices = [MagicMock()]
        mock_cleanup_response.choices[0].message.content = "This is the cleaned up transcript."

        # Configure mock to return different responses for each call
        mock_client.chat.completions.create.side_effect = [
            mock_summary_response,
            mock_cleanup_response
        ]

        # Call the function
        test_transcript = "uhm so this is a test transcript with filler words"
        summary, cleaned = openai_cleanup(test_transcript, 'test_video_123')

        # Verify results
        self.assertEqual(summary, "This is a test summary of the video.")
        self.assertEqual(cleaned, "This is the cleaned up transcript.")

        # Verify OpenAI client was instantiated with API key
        mock_openai_class.assert_called_once_with(api_key='test_api_key')

        # Verify chat.completions.create was called twice
        self.assertEqual(mock_client.chat.completions.create.call_count, 2)

        # Verify the calls were made with correct parameters
        calls = mock_client.chat.completions.create.call_args_list

        # First call should be for summarization
        first_call = calls[0]
        self.assertEqual(first_call.kwargs['model'], 'gpt-4o-mini')
        self.assertEqual(first_call.kwargs['temperature'], 0.7)
        self.assertIn('summarize', first_call.kwargs['messages'][0]['content'].lower())
        self.assertEqual(first_call.kwargs['messages'][1]['content'], test_transcript)

        # Second call should be for cleanup
        second_call = calls[1]
        self.assertEqual(second_call.kwargs['model'], 'gpt-4o-mini')
        self.assertIn('clean', second_call.kwargs['messages'][0]['content'].lower())

    @patch('transcripts.openai_key', '')
    def test_openai_cleanup_no_api_key(self):
        """Test openai_cleanup when no API key is available"""
        test_transcript = "test transcript"
        summary, cleaned = openai_cleanup(test_transcript, 'test_video_123')

        # Verify it returns defaults when no API key
        self.assertEqual(summary, "Summary not available")
        self.assertIsNone(cleaned)


if __name__ == '__main__':
    unittest.main()