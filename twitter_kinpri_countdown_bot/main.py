#!/usr/bin/env python3
import datetime
import argparse

from dateutil.parser import parse

from get_tweepy import get_api


# if now is 00:00:00, remaining days would be greater than 1 day
# so we must minus 1
RELEASE_DATE = parse('2017-06-10') - datetime.timedelta(seconds=1)


def get_remaining_days(now=None):
    if now is None:
        now = datetime.datetime.now()
    delta = RELEASE_DATE - now
    remaining = delta.days + 1
    return remaining


def tweet(screen_name='kinpricountdown'):
    api = get_api(screen_name)
    days = get_remaining_days()
    text = get_text(days)
    return api.update_status(text)


def get_text(days):
    # make the number of exclamation marks different
    # depanding on the remaining days
    if days % 10 == 0 or abs(days) < 10:
        exclamation_num = 2
    else:
        exclamation_num = 1
    exclamation = '！' * exclamation_num

    # add an additinal space character when afternoon
    # to avoid a duplicate status restriction
    if datetime.datetime.now().hour >= 12:
        space = ' '
    else:
        space = ''

    if days > 0:
        text = ('『KING OF PRISM -PRIDE the HERO-』公開まで、'
                'あと {days} 日です{exclamation} {space}#kinpri').format(
                    days=days, exclamation=exclamation, space=space)
    elif days == 0:
        text = ('✨🎉🌈 ！！！今日は『KING OF PRISM -PRIDE the HERO-』の'
                '公開日です！！！ 🌈🎉✨ {space}#kinpri').format(space=space)
    else:
        days *= -1
        text = ('『KING OF PRISM -PRIDE the HERO-』公開から、'
                '{days} 日が経過しました{exclamation} {space}#kinpri').format(
                    days=days, exclamation=exclamation, space=space)
    return text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', '-d', action='store_true')
    args = parser.parse_args()

    if args.debug:
        tweet('sakuramochi_pre')
    else:
        tweet()
