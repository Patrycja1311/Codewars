def is_smooth(arr):
    n = len(arr)
    mid = arr[n // 2] if n % 2 else arr[n // 2 - 1] + arr[n // 2]
    return arr[0] == arr[-1] == mid

