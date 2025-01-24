from datetime import datetime, timedelta


def date_nb_days(a0, a, p):
    daily_rate = p / 36000
    days = 0
    while a0 < a:
        a0 += a0 * daily_rate
        days += 1
    return (datetime(2016, 1, 1) + timedelta(days=days)).strftime("%Y-%m-%d")
