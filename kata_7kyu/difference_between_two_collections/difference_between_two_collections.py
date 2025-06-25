from collections import Counter


def diff(a, b):
    ca, cb = Counter(a), Counter(b)
    return sorted([x for x in set(a + b) if (x in ca) ^ (x in cb)])
