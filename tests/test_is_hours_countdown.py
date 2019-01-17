from twitter_kinpri_countdown_bot import is_publish_in_24_hours


class TestIsHoursCountdown:

    def test_just_time(self):
        """公開時間ちょうどの場合"""
        assert is_publish_in_24_hours(0) is True

    def test_is_18_hours_before(self):
        """18 時間前の場合"""
        assert is_publish_in_24_hours(18) is True

    def test_is_24_hours_before(self):
        """18 時間前の場合"""
        assert is_publish_in_24_hours(24) is False

    def test_is_25_hours_before(self):
        """18 時間前の場合"""
        assert is_publish_in_24_hours(25) is False
