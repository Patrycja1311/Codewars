def cube_odd(arr):
    if not all(isinstance(num, (int, float)) and not isinstance(num, bool) for num in arr):
        return None

    return sum(num ** 3 for num in arr if num % 2 != 0)
