import datetime
from dateutil.parser import parse
from twitter_kinpri_countdown_bot import get_remaining_days, get_remaining_hours, get_text, WORK_NAME


class TestGetRemainingDays:

    def test_specs(self):
        assert get_remaining_days() == \
               (parse('2019-03-02') - datetime.datetime.now()).days + 1

    def test_10days_before(self):
        assert get_remaining_days(parse('2019-02-20 0:0:0')) == 10

    def test_10days_before_plus_1sec(self):
        assert get_remaining_days(parse('2019-02-20 0:0:10')) == 10

    def test_10days_before_at_noon(self):
        assert get_remaining_days(parse('2019-02-20 12:0:10')) == 10

    def test_just_day_plus_1sec(self):
        assert get_remaining_days(parse('2019-03-02 0:0:10')) == 0

    def test_just_day(self):
        assert get_remaining_days(parse('2019-03-02 0:0:0')) == 0

    def test_10days_after(self):
        assert get_remaining_days(parse('2019-03-12 0:0:0')) == -10

    def test_10days_after_plus_1sec(self):
        assert get_remaining_days(parse('2019-03-12 0:0:10')) == -10


class TestGetRemainingHours:

    def test_1days_before(self):
        assert get_remaining_hours(parse('2019-03-01 00:00:00')) == 24

    def test_12hours_before(self):
        assert get_remaining_hours(parse('2019-03-01 12:00:00')) == 12

    def test_12hours_30min_before(self):
        assert get_remaining_hours(parse('2019-03-01 12:30:00')) == 11

    def test_23hours_before(self):
        assert get_remaining_hours(parse('2019-03-01 01:00:00')) == 23

    def test_2days_before(self):
        assert get_remaining_hours(parse('2019-02-28 00:00:00')) == 48

    def test_1days_before_plus_10_min(self):
        assert get_remaining_hours(parse('2019-02-28 23:50:00')) == 24

    def test_10days_before_at_noon(self):
        assert get_remaining_hours(parse('2019-02-20 12:00:00')) == 240 - 12

    def test_just_day_plus_1sec(self):
        assert get_remaining_hours(parse('2019-03-02 00:00:01')) == 0

    def test_just_day(self):
        assert get_remaining_hours(parse('2019-03-02 0:0:0')) == 0

    def test_10days_after(self):
        assert get_remaining_hours(parse('2019-03-12 0:0:0')) == -240

    def test_10days_after_plus_1sec(self):
        assert get_remaining_hours(parse('2019-03-12 0:0:10')) == -240


class TestGetText:

    @staticmethod
    def get_space():
        return ' ' * (datetime.datetime.now().hour // 6 % 4)

    def test_11days_before(self):
        text = get_text(11, 264)
        space = self.get_space()
        assert text == (
            f'{WORK_NAME}\n'
            '公開まで、あと 11 日です！\n'
            '공개까지 앞으로 11 일입니다!\n'
            f'{space}#kinpri #prettyrhythm'
        )

    def test_10days_before(self):
        text = get_text(10, 240)
        space = self.get_space()
        assert text == (
            f'{WORK_NAME}\n'
            '公開まで、あと 10 日です！！！\n'
            '공개까지 앞으로 10 일입니다!!!\n'
            f'{space}#kinpri #prettyrhythm'
        )

    def test_1days_before(self):
        text = get_text(1, 24)
        space = self.get_space()
        assert text == (
            f'{WORK_NAME}\n'
            '公開まで、あと 1 日です！！！\n'
            '공개까지 앞으로 1 일입니다!!!\n'
            f'{space}#kinpri #prettyrhythm'
        )

    def test_just_day(self):
        text = get_text(0, 0)
        space = self.get_space()
        assert text == (
            f'✨🎉🌈 {WORK_NAME} 🌈🎉✨\n'
            '公開日です！！！！！\n'
            '공개 일입니다!!!!!\n'
            f'{space}#kinpri #prettyrhythm'
        )

    def test_10days_after(self):
        text = get_text(-10, -240)
        space = self.get_space()
        assert text == (
            f'\n{WORK_NAME}\n'
            '今日は公開 10 日目です！！\n'
            '오늘은 공개 10 일째입니다!!\n'
            f'{space}#kinpri #prettyrhythm'
        )

    def test_11days_after(self):
        text = get_text(-11, -264)
        space = self.get_space()
        assert text == (
            f'\n{WORK_NAME}\n'
            '今日は公開 11 日目です！\n'
            '오늘은 공개 11 일째입니다!\n'
            f'{space}#kinpri #prettyrhythm'
        )
