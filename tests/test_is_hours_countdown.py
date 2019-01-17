from twitter_kinpri_countdown_bot import is_hours_countdown


class TestIsHoursCountdown:

    def test_is_midnight(self):
        """0:00 の場合"""
        assert is_hours_countdown(0) is False

    def test_is_not_midnight(self):
        """18:00 の場合"""
        assert is_hours_countdown(18) is True
