import re


def calculate(s):
    return str(eval(re.sub(r'plus', '+', re.sub(r'minus', '-', s))))
