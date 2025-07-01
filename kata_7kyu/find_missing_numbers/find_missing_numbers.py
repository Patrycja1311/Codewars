def find_missing_numbers(arr):
    if not arr or len(arr) < 2:
        return []
    return [x for x in range(arr[0], arr[-1]) if x not in arr]
