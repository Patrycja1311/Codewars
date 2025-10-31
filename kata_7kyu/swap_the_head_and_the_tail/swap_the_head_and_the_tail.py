def swap_head_tail(arr):
    m = len(arr)//2
    return arr[m+len(arr) % 2:] + arr[m:m+len(arr) % 2] + arr[:m]
