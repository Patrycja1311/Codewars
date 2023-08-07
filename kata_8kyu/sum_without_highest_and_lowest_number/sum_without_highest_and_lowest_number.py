def sum_array(arr):
    if arr == None:
        return 0
    elif len(arr) > 1:
        return sum(arr) - min(arr) - max(arr)
    else:
        return 0
