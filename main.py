#!/usr/bin/env python3
import datetime

from dateutil.parser import parse

from get_tweepy import get_api


def get_remaining_days():
    release_data = parse('2017-06-10')
    delta = release_data - datetime.datetime.now()
    remaining = delta.days + 1
    return remaining


def tweet():
    api = get_api('kinpricountdown')
    days = get_remaining_days()
    text = ('『KING OF PRISM -PRIDE the HERO-』公開まで、'
            'あと {days} 日です！ #kinpri').format(days=days)
    api.update_status(text)


if __name__ == '__main__':
    tweet()
