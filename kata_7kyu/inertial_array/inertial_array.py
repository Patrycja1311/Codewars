def is_inertial(arr):
    if not arr:
        return False
    max_val = max(arr)
    odd_values = [x for x in arr if x % 2 != 0]
    even_values = [x for x in arr if x % 2 == 0 and x != max_val]
    return (odd_values and max_val % 2 == 0 and
            all(odd > even for odd in odd_values for even in even_values))
