import re


def to_cents(amount):
    return int(amount[1:].replace('.', '')) if re.fullmatch(r'\$\d+\.\d{2}', amount) else None
