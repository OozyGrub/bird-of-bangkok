from datetime import timedelta, datetime, timezone

tz = timezone(timedelta(hours=7))


def as_bkk_tz(dt: datetime):
    return (dt - timedelta(hours=7)).astimezone(tz)


def get_start_of_day():
    return as_bkk_tz((datetime.today() + timedelta(hours=7)).replace(hour=0, minute=0, second=0, microsecond=0))


def is_between_yesterday(x: datetime):
    today = get_start_of_day()
    yesterday = today - timedelta(days=1)
    return x >= yesterday and x <= today
