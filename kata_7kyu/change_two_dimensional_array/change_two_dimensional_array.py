def matrix(array):
    return [[0 if i == j and val < 0 else 1 if i == j else val
             for j, val in enumerate(row)]
            for i, row in enumerate(array)]
