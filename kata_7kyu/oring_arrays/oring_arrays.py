def or_arrays(arr1, arr2, default=0):
    length = max(len(arr1), len(arr2))
    result = []
    for i in range(length):
        a = arr1[i] if i < len(arr1) else default
        b = arr2[i] if i < len(arr2) else default
        result.append(a | b)
    return result
