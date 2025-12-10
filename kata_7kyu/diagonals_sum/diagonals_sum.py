def sum_diagonals(matrix):
    return sum(matrix[i][i] + matrix[i][-1-i] for i in range(len(matrix)))
