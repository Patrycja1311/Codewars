import re


def is_vowel(s):
    if isinstance(s, str) and len(s) == 1:
        pattern = r'^[aeiouAEIOU]$'
        return bool(re.match(pattern, s))
    return False
