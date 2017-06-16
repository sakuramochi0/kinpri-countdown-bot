import datetime
from dateutil.parser import parse
from twitter_kinpri_countdown_bot import get_remaining_days, get_remaining_hours, get_text


class TestGetRemainingDays:

    def test_specs(self):
        assert get_remaining_days() == \
            (parse('2017-06-10') - datetime.datetime.now()).days + 1

    def test_10days_before(self):
        assert get_remaining_days(parse('2017-05-31 0:0:0')) == 10

    def test_10days_before_plus_1sec(self):
        assert get_remaining_days(parse('2017-05-31 0:0:10')) == 10

    def test_10days_before_at_noon(self):
        assert get_remaining_days(parse('2017-05-31 12:0:10')) == 10

    def test_just_day_plus_1sec(self):
        assert get_remaining_days(parse('2017-06-10 0:0:10')) == 0

    def test_just_day(self):
        assert get_remaining_days(parse('2017-06-10 0:0:0')) == 0

    def test_10days_after(self):
        assert get_remaining_days(parse('2017-06-20 0:0:0')) == -10

    def test_10days_after_plus_1sec(self):
        assert get_remaining_days(parse('2017-06-20 0:0:10')) == -10


class TestGetRemainingHours:

    def test_1days_before(self):
        assert get_remaining_hours(parse('2017-06-09 0:0:0')) == 24

    def test_12hours_before(self):
        assert get_remaining_hours(parse('2017-06-09 12:0:0')) == 12

    def test_12hours_30min_before(self):
        assert get_remaining_hours(parse('2017-06-09 12:30:0')) == 11

    def test_23hours_before(self):
        assert get_remaining_hours(parse('2017-06-09 1:0:0')) == 23

    def test_2days_before(self):
        assert get_remaining_hours(parse('2017-06-08 0:0:0')) == 48

    def test_1days_before_plus_10_min(self):
        assert get_remaining_hours(parse('2017-06-08 23:50:00')) == 24

    def test_10days_before_at_noon(self):
        assert get_remaining_hours(parse('2017-05-31 12:0:10')) == 240 - 12

    def test_just_day_plus_1sec(self):
        assert get_remaining_hours(parse('2017-06-10 0:0:10')) == 0

    def test_just_day(self):
        assert get_remaining_hours(parse('2017-06-10 0:0:0')) == 0

    def test_10days_after(self):
        assert get_remaining_hours(parse('2017-06-20 0:0:0')) == -240

    def test_10days_after_plus_1sec(self):
        assert get_remaining_hours(parse('2017-06-20 0:0:10')) == -240


class TestGetText:

    def get_space(self):
        return ' ' * (datetime.datetime.now().hour // 6 % 4)
        
    def test_11days_before(self):
        text = get_text(11, 264)
        space = self.get_space()
        assert text == ('『KING OF PRISM -PRIDE the HERO-』\n'
                        '公開まで、あと 11 日です！\n'
                        '공개까지 앞으로 11 일입니다!\n'
                        '{}#kinpri #prettyrhythm'.format(space))

    def test_10days_before(self):
        text = get_text(10, 240)
        space = self.get_space()
        assert text == ('『KING OF PRISM -PRIDE the HERO-』\n'
                        '公開まで、あと 10 日です！！！\n'
                        '공개까지 앞으로 10 일입니다!!!\n'
                        '{}#kinpri #prettyrhythm'.format(space))

    def test_1days_before(self):
        text = get_text(1, 24)
        space = self.get_space()
        assert text == ('『KING OF PRISM -PRIDE the HERO-』\n'
                        '公開まで、あと 1 日です！！！\n'
                        '공개까지 앞으로 1 일입니다!!!\n'
                        '{}#kinpri #prettyrhythm'.format(space))

    def test_25hours_before(self):
        text = get_text(1, 25)
        space = self.get_space()
        assert text == ('『KING OF PRISM -PRIDE the HERO-』\n'
                        '公開まで、あと 25 時間です！！！\n'
                        '공개까지 앞으로 25 시간입니다!!!\n'
                        '{}#kinpri #prettyrhythm'.format(space))

    def test_just_day(self):
        text = get_text(0, 0)
        space = self.get_space()
        assert text == \
            ('✨🎉🌈 『KING OF PRISM -PRIDE the HERO-』 🌈🎉✨\n'
             '公開日です！！！！！\n'
             '공개 일입니다!!!!!\n'
             '{}#kinpri #prettyrhythm'.format(space))

    def test_10days_after(self):
        text = get_text(-10, -240)
        space = self.get_space()
        assert text == ('『KING OF PRISM -PRIDE the HERO-』\n'
                        '公開から、10 日が経過しました！！\n'
                        '개봉 후 10 일 경과했습니다!!\n'
                        '{}#kinpri #prettyrhythm'.format(space))

    def test_11days_after(self):
        text = get_text(-11, -264)
        space = self.get_space()
        assert text == ('『KING OF PRISM -PRIDE the HERO-』\n'
                        '公開から、11 日が経過しました！\n'
                        '개봉 후 11 일 경과했습니다!\n'
                        '{}#kinpri #prettyrhythm'.format(space))
