def next_letter(s):
    result = []
    for c in s:
        if 'a' <= c <= 'z':
            result.append(chr((ord(c) - 96) % 26 + 97))
        elif 'A' <= c <= 'Z':
            result.append(chr((ord(c) - 64) % 26 + 65))
        else:
            result.append(c)
    return ''.join(result)
