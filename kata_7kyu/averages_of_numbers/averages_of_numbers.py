def averages(arr):
    return [(arr[i] + arr[i+1]) / 2 for i in range(len(arr) - 1)] if arr and len(arr) > 1 else []
