#!/usr/bin/env python3
import datetime
import argparse

from dateutil.parser import parse

from get_tweepy import get_api


# if now is 00:00:00, remaining days would be greater than 1 day
# so we must minus 1
RELEASE_DATE = parse('2017-06-10') - datetime.timedelta(seconds=1)
RELEASE_DATETIME = parse('2017-06-10 00:00') - datetime.timedelta(seconds=1)


def get_remaining_days(now=None):
    if now is None:
        now = datetime.datetime.now()
    delta = RELEASE_DATE - now
    remaining = delta.days + 1
    return remaining


def get_remaining_hours(now=None):
    if now is None:
        now = datetime.datetime.now()
    # see the same hour if within 30 min.
    delta = RELEASE_DATETIME - now
    if delta >= datetime.timedelta(0):
        delta += datetime.timedelta(minutes=30)
    else:
        delta -= datetime.timedelta(minutes=30)
    remaining = int(delta.total_seconds() / 3600)
    return remaining


def tweet(screen_name='kinpricountdown'):
    api = get_api(screen_name)
    days = get_remaining_days()
    hours = get_remaining_hours()
    text = get_text(days, hours)
    img = get_img(days)
    if not is_hours_countdown(hours) and img:
        res = api.update_with_media(img, status=text)
    else:
        res = api.update_status(text)
    return res


def get_img(days):
    # prepare images if 0 <= days <= 5
    if 0 <= days <= 5:
        img = 'img/kinpri-countdown-{}.png'.format(days)
    else:
        img = None
    return img


def is_hours_countdown(hours):
    return hours % 24 != 0


def get_text(days, hours):
    # make the number of exclamation marks different
    # depanding on the remaining days
    if 0 < days <= 10:
        exclamation_num = 3
    elif days % 10 == 0:
        exclamation_num = 2
    else:
        exclamation_num = 1
    exclamation = '！' * exclamation_num
    exclamation_ko = '!' * exclamation_num

    # add an additinal space characters
    # to avoid a duplicate status restriction
    # there are 4 cases: 0-6 / 6-12 / 12-18 / 18-24
    space = ' ' * (datetime.datetime.now().hour // 6 % 4)

    if days > 0:
        if is_hours_countdown(hours):
            text = ('『KING OF PRISM -PRIDE the HERO-』\n'
                    '公開まで、あと {hours} 時間です{exclamation}\n'
                    '공개까지 앞으로 {hours} 시간입니다{exclamation_ko}\n'
                    '#kinpri #prettyrhythm').format(
                        hours=hours,
                        exclamation=exclamation,
                        exclamation_ko=exclamation_ko,
                    )
        else:
            text = ('『KING OF PRISM -PRIDE the HERO-』\n'
                    '公開まで、あと {days} 日です{exclamation}\n'
                    '공개까지 앞으로 {days} 일입니다{exclamation_ko}\n'
                    '{space}#kinpri #prettyrhythm').format(
                        days=days,
                        exclamation=exclamation,
                        exclamation_ko=exclamation_ko,
                        space=space)
    elif days == 0:
        text = ('✨🎉🌈 『KING OF PRISM -PRIDE the HERO-』 🌈🎉✨\n'
                '公開日です！！！！！\n'
                '공개 일입니다!!!!!\n'
                '{space}#kinpri #prettyrhythm').format(space=space)
    else:
        days *= -1
        text = ('『KING OF PRISM -PRIDE the HERO-』\n'
                '公開から、{days} 日が経過しました{exclamation}\n'
                '개봉 후 {days} 일 경과했습니다{exclamation_ko}\n'
                '{space}#kinpri #prettyrhythm').format(
                    days=days,
                    exclamation=exclamation,
                    exclamation_ko=exclamation_ko,
                    space=space)
    return text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', '-d', action='store_true')
    args = parser.parse_args()

    if args.debug:
        tweet('sakuramochi_pre')
    else:
        tweet()
