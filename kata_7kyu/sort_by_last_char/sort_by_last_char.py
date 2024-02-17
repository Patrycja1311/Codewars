def last(s):
    words = s.split()
    return sorted(words, key=lambda x: (x[-1], words.index(x)))
