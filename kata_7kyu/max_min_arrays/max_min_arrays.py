def solve(arr):
    sorted_arr = sorted(arr)
    return [sorted_arr[-(i+1)//2] if i % 2 == 0 else sorted_arr[i//2] for i in range(len(arr))]
