def is_zero_balanced(arr):
    if not arr or sum(arr) != 0:
        return False
    for num in arr:
        if num > 0 and -num not in arr:
            return False
    return True
