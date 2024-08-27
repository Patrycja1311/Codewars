import re


def unscramble_eggs(word):
    return re.sub(r'([b-df-hj-np-tv-z])egg', r'\1', word, flags=re.IGNORECASE)
