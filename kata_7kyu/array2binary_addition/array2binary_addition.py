def arr2bin(arr):
    return bin(sum(arr))[2:] if all(isinstance(x, int) for x in arr) else False
