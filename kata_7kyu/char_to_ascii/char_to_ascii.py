def char_to_ascii(s):
    if not s:
        return None
    result = {}
    for char in s:
        if char.isalpha() and char not in result:
            result[char] = ord(char)
    return result
