def freq_seq(s, sep):
    return f'{sep}'.join([f"{s.count(i)}" for i in s])
