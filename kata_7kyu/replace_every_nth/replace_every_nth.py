def replace_nth(text, n, old_value, new_value):
    if n <= 0:
        return text
    count = 0
    result = []
    for c in text:
        if c == old_value:
            count += 1
            result.append(new_value if count % n == 0 else c)
        else:
            result.append(c)
    return ''.join(result)
