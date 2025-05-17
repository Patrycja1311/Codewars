def shift_left(a, b):
    i, j = len(a) - 1, len(b) - 1
    common_suffix_length = 0

    while i >= 0 and j >= 0 and a[i] == b[j]:
        common_suffix_length += 1
        i -= 1
        j -= 1

    return (len(a) - common_suffix_length) + (len(b) - common_suffix_length)
