def solution(mtrx):
    n = len(mtrx)
    for i in range(n):
        for j in range(n):
            if mtrx[i][j] == '>':
                for k in range(j + 1, n):
                    if mtrx[i][k] == 'x':
                        return True
                return False
