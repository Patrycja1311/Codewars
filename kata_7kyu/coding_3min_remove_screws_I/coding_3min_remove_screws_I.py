def sc(s):
    return len(s) + (len(s) - 1) + s.count('+-') * 5 + s.count('-+') * 5
