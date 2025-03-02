def median(array):
    array.sort()
    n = len(array)
    mid = n // 2
    return array[mid] if n % 2 else (array[mid - 1] + array[mid]) / 2
