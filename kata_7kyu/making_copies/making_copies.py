def copy_list(l):
    if not isinstance(l, list):
        raise TypeError("Input must be a list")
    return l.copy()
