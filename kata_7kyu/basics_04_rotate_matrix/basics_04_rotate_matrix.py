def rotate_matrix(arr):
    return list(map(list, zip(*arr)))[::-1]
