def create_box(m, n):
    return [[min(i, j, n-1-i, m-1-j) + 1 for j in range(m)] for i in range(n)]
