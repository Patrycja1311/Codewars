def x_marks_the_spot(mat):
    pos = [(r, c) for r, row in enumerate(mat) for c, v in enumerate(row) if v == 'x']
    return list(pos[0]) if len(pos) == 1 else []
