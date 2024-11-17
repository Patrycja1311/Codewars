def min_min_max(arr):
    smallest, largest = min(arr), max(arr)
    minimumAbsent = next(num for num in range(smallest, largest + 1) if num not in arr)
    return [smallest, minimumAbsent, largest]
