def scramble(strng, array):
    result = [''] * len(strng)
    for i, index in enumerate(array):
        result[index] = strng[i]
    return ''.join(result)
