def consecutive(arr, a, b):
    index_a = arr.index(a)
    index_b = arr.index(b)
    return abs(index_a - index_b) == 1
