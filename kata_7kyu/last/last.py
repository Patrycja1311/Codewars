def last(*args):
    return args[0][-1] if len(args) == 1 and isinstance(args[0], (list, str)) else args[-1]
