def pairs(arr):
    return sum(abs(arr[i] - arr[i + 1]) == 1 for i in range(0, len(arr) - 1, 2))
