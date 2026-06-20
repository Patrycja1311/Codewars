import re


def solve(eq):
    return ''.join(re.findall(r'\w+|[+\-*/]', eq)[::-1])
