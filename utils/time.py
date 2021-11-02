from datetime import timedelta, datetime, timezone

tz = timezone(timedelta(hours=7))


def as_bkk_tz(dt: datetime):
    return (dt - timedelta(hours=7)).astimezone(tz)


def get_start_of_day():
    return as_bkk_tz((datetime.today() + timedelta(hours=7)).replace(hour=0, minute=0, second=0, microsecond=0))


def get_start_of_hour():
    return as_bkk_tz((datetime.today() + timedelta(hours=7)).replace(minute=0, second=0, microsecond=0))


def is_between_yesterday(x: datetime):
    today = get_start_of_day()
    yesterday = today - timedelta(days=1)
    return x >= yesterday and x <= today


def is_between_previous_hrs(x: datetime):
    current_hour = get_start_of_hour()
    previous_hour = current_hour - timedelta(hours=1)
    return x >= previous_hour and x <= current_hour
