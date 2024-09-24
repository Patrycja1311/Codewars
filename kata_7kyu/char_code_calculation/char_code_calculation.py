def calc(x):
    total1 = ''.join(str(ord(c)) for c in x)
    return sum(int(d) for d in total1) - sum(int(d) for d in total1.replace('7', '1'))
