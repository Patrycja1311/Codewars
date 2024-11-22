def numbers(*args):
    return all(isinstance(arg, (int, float)) and not isinstance(arg, bool) for arg in args)
