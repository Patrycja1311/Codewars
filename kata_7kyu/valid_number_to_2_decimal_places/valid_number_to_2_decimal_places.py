import re


def valid_number(n):
    return bool(re.fullmatch(r'[+-]?(\d*)\.\d{2}', n))
