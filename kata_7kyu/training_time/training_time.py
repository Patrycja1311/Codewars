def shuffle_it(arr, *swaps):
    arr = arr[:]
    for i, j in swaps:
        arr[i], arr[j] = arr[j], arr[i]
    return arr
