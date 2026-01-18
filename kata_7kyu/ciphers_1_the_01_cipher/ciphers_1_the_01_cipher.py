def encode(s):
    result = []
    for ch in s:
        if ch.isalpha():
            index = ord(ch.lower()) - ord('a')
            result.append('1' if index % 2 == 1 else '0')
        else:
            result.append(ch)
    return ''.join(result)
