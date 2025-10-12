import re


def timed_reading(max_length, text):
    return sum(len(w) <= max_length for w in re.findall(r'[A-Za-z]+', text))
