def remove_duplicate_words(s):
    result = []
    for i in s.split():
        if i not in result:
            result.append(i)
    return ' '.join(result)
