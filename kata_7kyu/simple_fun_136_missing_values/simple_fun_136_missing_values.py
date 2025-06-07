from collections import Counter


def missing_values(seq):
    return (lambda c: next(k for k, v in c.items() if v == 1)**2 * next(k for k, v in c.items() if v == 2))(Counter(seq))
