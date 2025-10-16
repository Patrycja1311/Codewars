import re


def rad_ladies(name):
    return re.sub(r'[^A-Za-z !]', '', name).upper()
