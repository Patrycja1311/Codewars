import string


def position(alphabet):
    letters = string.ascii_lowercase
    return f'Position of alphabet: {letters.index(alphabet.lower()) + 1}'
