def main_diagonal_product(mat):
    return eval('*'.join(str(mat[i][i]) for i in range(len(mat))))
