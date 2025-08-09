def diagonal(matrix):
    p, s = sum(matrix[i][i] for i in range(len(matrix))), sum(matrix[i][-i-1] for i in range(len(matrix)))
    return "Principal Diagonal win!" if p > s else "Secondary Diagonal win!" if s > p else "Draw!"
