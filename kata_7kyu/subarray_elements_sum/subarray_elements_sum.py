def elements_sum(arr, d=0):
    n = len(arr)
    return sum(arr[i][n - i - 1] if n - i - 1 < len(arr[i]) else d for i in range(n))
 w 