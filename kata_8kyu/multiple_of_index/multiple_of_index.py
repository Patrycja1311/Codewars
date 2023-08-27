def multiple_of_index(arr):
    new_arr = []
    for i, num in enumerate(arr):
        if i != 0 and num % i == 0 or i == 0 and num == 0:
            new_arr.append(num)
    return new_arr
