def find_even_index(arr):
    total_sum = sum(arr)
    left_side = 0
    for index in range(len(arr)):
        if left_side == total_sum - left_side - arr[index]:
            return index
        left_side += arr[index]
    return -1
