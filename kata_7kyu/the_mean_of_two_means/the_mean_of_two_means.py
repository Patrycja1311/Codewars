def get_mean(arr, x, y):
    if x <= 1 or y <= 1 or x > len(arr) or y > len(arr):
        return -1
    return (sum(arr[:x]) / x + sum(arr[-y:]) / y) / 2
