import re


def validate_time(time):
    return bool(re.fullmatch(r'(?:[01]?\d|2[0-3]):[0-5]\d', time))
