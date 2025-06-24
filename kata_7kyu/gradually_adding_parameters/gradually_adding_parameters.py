def add(*args):
    return sum(val * (i + 1) for i, val in enumerate(args))
