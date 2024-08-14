def smaller(arr):
    return [sum(x < arr[i] for x in arr[i+1:]) for i in range(len(arr))]
