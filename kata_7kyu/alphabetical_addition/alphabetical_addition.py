def add_letters(*letters):
    return chr((sum(ord(letter) - 96 for letter in letters) % 26 or 26) + 96)
