def small_enough(a, limit):
    if not a:
        return True
    return a[0] <= limit and small_enough(a[1:], limit)
