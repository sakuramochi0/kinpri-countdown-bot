import argparse
import datetime

from dateutil.parser import parse
# noinspection PyUnresolvedReferences
from get_tweepy import get_api

# if now is 00:00:00, remaining days would be greater than 1 day
# so we must minus 1
RELEASE_DATE = parse('2019-03-23') - datetime.timedelta(seconds=1)
RELEASE_DATETIME = parse('2019-03-23 00:00') - datetime.timedelta(seconds=1)
#WORK_NAME = '『KING OF PRISM -Shiny Seven Stars- I プロローグ×ユキノジョウ×タイガ』'
WORK_NAME = '『KING OF PRISM -Shiny Seven Stars- II カケル×ジョージ×ミナト』'
#WORK_NAME = '『KING OF PRISM -Shiny Seven Stars- III レオ×ユウ×アレク』'
#WORK_NAME = '『KING OF PRISM -Shiny Seven Stars- IV ルヰ×シン×Unknown』'


def get_remaining_days(now=None):
    """公開日までの残り日数を取得する。"""
    if now is None:
        now = datetime.datetime.now()
    delta = RELEASE_DATE - now
    remaining = delta.days + 1
    return remaining


def get_remaining_hours(now=None):
    """公開日の 0:00 までの残り時間を計算する。"""
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


def tweet():
    """実際にツイートを行う。"""
    days = get_remaining_days()
    hours = get_remaining_hours()
    text = get_text(days, hours)
    img = None
    if not is_publish_in_24_hours(hours) and img:
        res = api.update_with_media(img, status=text)
    else:
        res = api.update_status(text)
    return res


def get_img(days):
    """公開直前画像のファイル名を取得する。"""
    # prepare images if 0 <= days <= 5
    if 0 <= days <= 5:
        img = 'img/kinpri-countdown-{}.png'.format(days)
    else:
        img = None
    return img


def is_publish_in_24_hours(hours: int) -> bool:
    """公開まで1日を切っているかどうか"""
    return hours < 24


def get_text(days: int, hours: int) -> str:
    """ツイートテキストを構築する。"""
    exclamation, exclamation_ko = get_exclamation_marks(days)
    get_exclamation_marks(days)

    # 100の倍数の時にクラッカーを鳴らす🎉✨
    if days % 100 == 0:
        celebration = '👑🌹🎉🌈✨'
    else:
        celebration = ''

    # 空白を追加することで、重複ツイートの制限を回避
    # 次の4つの時間帯に分ける: 0-6 / 6-12 / 12-18 / 18-24
    space = ' ' * (datetime.datetime.now().hour // 6 % 4)

    if days > 0:
        # 公開前
        if is_publish_in_24_hours(hours):
            text = (
                f'{WORK_NAME}\n'
                f'公開まで、あと {hours} 時間です{exclamation}\n'
                f'공개까지 앞으로 {hours} 시간입니다{exclamation_ko}\n'
                '#kinpri #prettyrhythm'
            )
        else:
            text = (
                f'{WORK_NAME}\n'
                f'公開まで、あと {days} 日です{exclamation}\n'
                f'공개까지 앞으로 {days} 일입니다{exclamation_ko}\n'
                f'{space}#kinpri #prettyrhythm'
            )
    elif days == 0:
        # 公開日当日
        text = (
            f'✨🎉🌈 {WORK_NAME} 🌈🎉✨\n'
            '公開日です！！！！！\n'
            '공개 일입니다!!!!!\n'
            f'{space}#kinpri #prettyrhythm'
        )
    else:
        # 公開後
        days *= -1
        text = (
            f'{celebration}\n'
            f'{WORK_NAME}\n'
            f'今日は公開 {days} 日目です{exclamation}\n'
            f'오늘은 공개 {days} 일째입니다{exclamation_ko}\n'
            f'{space}#kinpri #prettyrhythm'
        )

    return text


def get_exclamation_marks(days: int) -> (str, str):
    """残り日数に応じて、数を変えた「！」を生成する"""
    if 0 < days <= 10:
        exclamation_num = 3
    elif days % 10 == 0:
        exclamation_num = 2
    else:
        exclamation_num = 1
    exclamation = '！' * exclamation_num
    exclamation_ko = '!' * exclamation_num
    return exclamation, exclamation_ko


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', '-d', action='store_true')
    args = parser.parse_args()

    screen_name = 'kinpricountdown'
    if args.debug:
        screen_name = 'sakuramochi_pre'
    api = get_api(screen_name)

    tweet()
