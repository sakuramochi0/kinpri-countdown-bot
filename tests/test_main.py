import datetime
from dateutil.parser import parse
from twitter_kinpri_countdown_bot import get_remaining_days, get_text


class TestGetRemainingDays:

    def test_specs(self):
        assert get_remaining_days() == \
            (parse('2017-06-10') - datetime.datetime.now()).days + 1

    def test_10days_before_plus_1sec(self):
        assert get_remaining_days(parse('2017-05-31 0:0:10')) == 10

    def test_10days_after_plus_1sec(self):
        assert get_remaining_days(parse('2017-06-20 0:0:10')) == -10

    def test_just_day_plus_1sec(self):
        assert get_remaining_days(parse('2017-06-10 0:0:10')) == 0

    def test_10days_before(self):
        assert get_remaining_days(parse('2017-05-31 0:0:0')) == 10

    def test_just_day(self):
        assert get_remaining_days(parse('2017-06-10 0:0:0')) == 0

    def test_10days_after(self):
        assert get_remaining_days(parse('2017-06-20 0:0:0')) == -10


class TestGetText:

    def test_11days_before(self):
        text = get_text(11)
        assert text == ('『KING OF PRISM -PRIDE the HERO-』公開まで、'
                        'あと 11 日です！ #kinpri')

    def test_10days_before(self):
        text = get_text(10)
        assert text == ('『KING OF PRISM -PRIDE the HERO-』公開まで、'
                        'あと 10 日です！！ #kinpri')

    def test_just_day(self):
        text = get_text(0)
        assert text == ('🎉🌈 今日は『KING OF PRISM -PRIDE the HERO-』の公開日です！！！ 🌈🎉'
                        ' #kinpri')

    def test_10days_after(self):
        text = get_text(-10)
        assert text == ('『KING OF PRISM -PRIDE the HERO-』公開から、'
                        '10 日が経過しました！！ #kinpri')

    def test_11days_after(self):
        text = get_text(-11)
        assert text == ('『KING OF PRISM -PRIDE the HERO-』公開から、'
                        '11 日が経過しました！ #kinpri')
