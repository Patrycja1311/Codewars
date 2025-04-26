def elimination(arr):
    return next((x for x in arr if arr.count(x) > 1), None)
