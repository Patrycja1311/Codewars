def phone_call(min1, min2_10, min11, s):
    if s < min1:
        return 0
    s -= min1
    m = 1 + min(9, s // min2_10)
    s = max(0, s - 9 * min2_10)
    return m + s // min11
