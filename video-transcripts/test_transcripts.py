import unittest
from transcripts import build_timeline_from_transcript, parse_timestamp_to_seconds, format_duration


class TestTimelineBuilder(unittest.TestCase):
    """Test the timeline building functionality for chapter generation."""
    
    def test_build_timeline_basic(self):
        """Test that timeline is built correctly from raw transcript data."""
        raw_transcript = [
            {'text': 'Hello everyone', 'start': 0, 'duration': 2},
            {'text': 'Welcome to the show', 'start': 2, 'duration': 3},
            {'text': 'Today we are talking about OpenTelemetry', 'start': 35, 'duration': 4},
            {'text': 'It is very exciting', 'start': 39, 'duration': 2},
        ]
        
        timeline = build_timeline_from_transcript(raw_transcript, sample_interval=30)
        
        # Should have entries at 00:00:00 and 00:00:30
        self.assertIn('[00:00:00]', timeline)
        self.assertIn('[00:00:30]', timeline)
        self.assertIn('Hello everyone', timeline)
        self.assertIn('OpenTelemetry', timeline)
    
    def test_build_timeline_filters_music(self):
        """Test that [Music] and similar markers are filtered out."""
        raw_transcript = [
            {'text': 'Hello everyone', 'start': 0, 'duration': 2},
            {'text': '[Music]', 'start': 2, 'duration': 5},
            {'text': '[Applause]', 'start': 7, 'duration': 3},
            {'text': 'Welcome back', 'start': 28, 'duration': 2},  # Within ±5 window of 30s
        ]
        
        timeline = build_timeline_from_transcript(raw_transcript, sample_interval=30)
        
        # Should not contain filtered markers
        self.assertNotIn('[Music]', timeline)
        self.assertNotIn('[Applause]', timeline)
        # Should contain actual speech
        self.assertIn('Hello everyone', timeline)
        self.assertIn('Welcome back', timeline)
    
    def test_build_timeline_empty_transcript(self):
        """Test that empty transcript returns empty timeline."""
        timeline = build_timeline_from_transcript([], sample_interval=30)
        self.assertEqual(timeline, "")
        
        timeline = build_timeline_from_transcript(None, sample_interval=30)
        self.assertEqual(timeline, "")
    
    def test_build_timeline_custom_interval(self):
        """Test that custom sample intervals work correctly."""
        raw_transcript = [
            {'text': 'Start', 'start': 0, 'duration': 1},
            {'text': 'At 10 seconds', 'start': 10, 'duration': 2},
            {'text': 'At 20 seconds', 'start': 20, 'duration': 2},
            {'text': 'At 30 seconds', 'start': 30, 'duration': 2},
        ]
        
        # Sample every 10 seconds
        timeline = build_timeline_from_transcript(raw_transcript, sample_interval=10)
        
        # Should have entries at 0, 10, 20, 30
        self.assertIn('[00:00:00]', timeline)
        self.assertIn('[00:00:10]', timeline)
        self.assertIn('[00:00:20]', timeline)
        self.assertIn('[00:00:30]', timeline)


    def test_build_timeline_preserves_precision(self):
        """Test that timeline captures precise timestamps, not just rounded intervals."""
        raw_transcript = [
            {'text': 'Starting at 3 seconds', 'start': 3, 'duration': 2},
            {'text': 'Now at 32 seconds', 'start': 32, 'duration': 2},
            {'text': 'And at 91 seconds', 'start': 91, 'duration': 2},
        ]
        
        # Sample every 30 seconds with ±5 second window
        # 0s sample (window 0-5) captures text at 3s
        # 30s sample (window 25-35) captures text at 32s
        # 90s sample (window 85-95) captures text at 91s
        timeline = build_timeline_from_transcript(raw_transcript, sample_interval=30)
        
        # Should capture text from the sampling points
        self.assertIn('[00:00:00]', timeline)
        self.assertIn('[00:00:30]', timeline)
        self.assertIn('[00:01:30]', timeline)
        # Verify text is captured at each sample point
        self.assertIn('3 seconds', timeline)
        self.assertIn('32 seconds', timeline)
        self.assertIn('91 seconds', timeline)


class TestYouTubeAPIErrorHandling(unittest.TestCase):
    """Test that YouTube API exceptions work as expected with our pinned version."""
    
    def test_youtube_api_exceptions_importable(self):
        """Test that all YouTube API exceptions we depend on can be imported.
        
        This will fail if the API changes in a way that breaks our imports.
        """
        # Import all exceptions we use
        from youtube_transcript_api import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
        from youtube_transcript_api._errors import YouTubeRequestFailed
        
        # Verify they're actual exception classes
        self.assertTrue(issubclass(TranscriptsDisabled, Exception))
        self.assertTrue(issubclass(NoTranscriptFound, Exception))
        self.assertTrue(issubclass(VideoUnavailable, Exception))
        self.assertTrue(issubclass(YouTubeRequestFailed, Exception))
    
    def test_youtube_api_exceptions_catchable(self):
        """Test that YouTube API exceptions can be caught.
        
        This validates that exceptions raised by the library can be caught
        and their error messages can be inspected (as our code does).
        """
        from youtube_transcript_api import TranscriptsDisabled, NoTranscriptFound
        
        # Test we can catch TranscriptsDisabled
        with self.assertRaises(TranscriptsDisabled):
            raise TranscriptsDisabled("video_id")
        
        # Test we can catch NoTranscriptFound
        with self.assertRaises(NoTranscriptFound):
            raise NoTranscriptFound("video_id", [], "en")


class TestTimestampParsing(unittest.TestCase):
    """Test timestamp parsing and formatting functions."""
    
    def test_parse_timestamp_to_seconds(self):
        """Test converting timestamp strings to seconds."""
        self.assertEqual(parse_timestamp_to_seconds('00:00:00'), 0)
        self.assertEqual(parse_timestamp_to_seconds('00:01:00'), 60)
        self.assertEqual(parse_timestamp_to_seconds('00:05:30'), 330)
        self.assertEqual(parse_timestamp_to_seconds('01:00:00'), 3600)
        self.assertEqual(parse_timestamp_to_seconds('01:23:45'), 5025)
        
        # Test MM:SS format
        self.assertEqual(parse_timestamp_to_seconds('05:30'), 330)
        self.assertEqual(parse_timestamp_to_seconds('1:00'), 60)
    
    def test_format_duration(self):
        """Test formatting seconds into HH:MM:SS."""
        self.assertEqual(format_duration(0), '00:00:00')
        self.assertEqual(format_duration(60), '00:01:00')
        self.assertEqual(format_duration(330), '00:05:30')
        self.assertEqual(format_duration(3600), '01:00:00')
        self.assertEqual(format_duration(5025), '01:23:45')
    
    def test_timestamp_roundtrip(self):
        """Test that parsing and formatting are inverse operations."""
        timestamps = ['00:00:00', '00:05:30', '01:23:45', '02:00:00']
        for ts in timestamps:
            seconds = parse_timestamp_to_seconds(ts)
            formatted = format_duration(seconds)
            self.assertEqual(formatted, ts)


if __name__ == '__main__':
    unittest.main()

