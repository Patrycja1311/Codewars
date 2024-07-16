def encode(message, key):
    key_digits = [int(d) for d in str(key)]
    return [(ord(char) - 96 + key_digits[i % len(key_digits)]) for i, char in enumerate(message)]
