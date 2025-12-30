def buy(x, arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == x:
                return [i, j]
    return None
