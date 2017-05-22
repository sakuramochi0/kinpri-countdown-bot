import datetime
from dateutil.parser import parse
from twitter_kinpri_countdown_bot import get_remaining_days, get_text


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


class TestGetText:

    def test_11days_before(self):
        text = get_text(11)
        if datetime.datetime.now().hour >= 12:
            assert text == ('『KING OF PRISM -PRIDE the HERO-』\n'
                            '公開まで、あと 11 日です！\n'
                            '공개까지 앞으로 11 일입니다!\n'
                            ' #kinpri')
        else:
            assert text == ('『KING OF PRISM -PRIDE the HERO-』\n'
                            '公開まで、あと 11 日です！\n'
                            '공개까지 앞으로 11 일입니다!\n'
                            '#kinpri')

    def test_10days_before(self):
        text = get_text(10)
        if datetime.datetime.now().hour >= 12:
            assert text == ('『KING OF PRISM -PRIDE the HERO-』\n'
                            '公開まで、あと 10 日です！！ \n'
                            '공개까지 앞으로 10 일입니다!!\n'
                            '#kinpri')
        else:
            assert text == ('『KING OF PRISM -PRIDE the HERO-』\n'
                            '公開まで、あと 10 日です！！\n'
                            '공개까지 앞으로 10 일입니다!!\n'
                            '#kinpri')

    def test_just_day(self):
        text = get_text(0)
        if datetime.datetime.now().hour >= 12:
            assert text == \
                ('✨🎉🌈 ！！！今日は『KING OF PRISM -PRIDE the HERO-』の公開日です！！！ 🌈🎉✨'
                 '  #kinpri')
        else:
                ('✨🎉🌈 ！！！今日は『KING OF PRISM -PRIDE the HERO-』の公開日です！！！ 🌈🎉✨'
                 ' #kinpri')

    def test_10days_after(self):
        text = get_text(-10)
        if datetime.datetime.now().hour >= 12:
            assert text == ('『KING OF PRISM -PRIDE the HERO-』\n'
                            '公開から、10 日が経過しました！！\n'
                            '개봉 후 10 일 경과했습니다!!\n'
                            ' #kinpri')
        else:
            assert text == ('『KING OF PRISM -PRIDE the HERO-』\n'
                            '公開から、10 日が経過しました！！\n'
                            '개봉 후 10 일 경과했습니다!!\n'
                            '#kinpri')

    def test_11days_after(self):
        text = get_text(-11)
        if datetime.datetime.now().hour >= 12:
            assert text == ('『KING OF PRISM -PRIDE the HERO-』\n'
                            '公開から、11 日が経過しました！\n'
                            '개봉 후 11 일 경과했습니다!\n'
                            ' #kinpri')
        else:
            assert text == ('『KING OF PRISM -PRIDE the HERO-』\n'
                            '公開から、11 日が経過しました！\n'
                            '개봉 후 11 일 경과했습니다!\n'
                            '#kinpri')
