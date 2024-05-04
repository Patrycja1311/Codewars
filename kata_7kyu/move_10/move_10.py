def move_ten(st):
    return ''.join(chr(((ord(char) - 97 if char.islower() else ord(char) - 65) + 10) % 26 + 97 if char.islower() else 65) if char.isalpha() else char for char in st)
