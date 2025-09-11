def min_and_max(l, d, x):
    s = lambda n: sum(map(int, str(n)))
    return [next(i for i in range(l, d+1) if s(i)==x),
            next(i for i in range(d, l-1, -1) if s(i)==x)]
