def reverse_invert(lst):
    return [-int(str(abs(x))[::-1]) if x > 0 else int(str(abs(x))[::-1]) for x in lst if type(x) is int]
