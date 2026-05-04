def is_sator_square(tablet):
    n = len(tablet)
    for i in range(n):
        for j in range(n):
            if not (
                    tablet[i][j] == tablet[j][i] ==
                    tablet[n - 1 - i][n - 1 - j]
            ):
                return False
    return True
