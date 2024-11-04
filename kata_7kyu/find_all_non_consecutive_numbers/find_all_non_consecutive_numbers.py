def all_non_consecutive(arr):
    return [{'i': i, 'n': arr[i]} for i in range(1, len(arr)) if arr[i] != arr[i - 1] + 1]
