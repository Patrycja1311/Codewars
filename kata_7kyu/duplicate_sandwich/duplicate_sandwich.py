def duplicate_sandwich(arr):
    x = next(i for i in arr if arr.count(i) > 1)
    return arr[arr.index(x) + 1: arr.index(x, arr.index(x) + 1)]
