def split_by_value(k, elements):
    less = [x for x in elements if x < k]
    more_or_equal = [x for x in elements if x >= k]
    return less + more_or_equal
