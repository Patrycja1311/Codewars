def find_next_power(val, pow_):
    from math import ceil
    return ceil(val**(1/pow_))**pow_
