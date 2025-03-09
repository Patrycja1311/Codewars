def sum_nested(lst):
    return sum(sum_nested(item) if isinstance(item, list) else item for item in lst)
