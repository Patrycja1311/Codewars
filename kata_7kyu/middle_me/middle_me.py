def middle_me(N, X, Y):
    return (Y * N)[:N//2] + X + (Y * N)[-N//2:] if N % 2 == 0 else X
