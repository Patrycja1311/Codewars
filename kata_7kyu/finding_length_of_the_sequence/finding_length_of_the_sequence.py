def length_of_sequence(arr,n):
    if arr.count(n) != 2:
        return 0
    start = arr.index(n)
    end = len(arr) - 1 - arr[::-1].index(n)
    return end - start + 1
