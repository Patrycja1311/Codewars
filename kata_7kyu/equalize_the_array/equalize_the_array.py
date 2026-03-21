def equalize(arr):
    if not arr:
        return []
    first = arr[0]
    return [f"{x - first:+d}" for x in arr]
