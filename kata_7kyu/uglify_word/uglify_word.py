def uglify_word(s):
    flag, result = 1, []
    for char in s:
        if char.isalpha():
            result.append(char.upper() if flag else char.lower())
            flag ^= 1  # Toggle flag
        else:
            result.append(char)
            flag = 1  # Reset flag
    return ''.join(result)
