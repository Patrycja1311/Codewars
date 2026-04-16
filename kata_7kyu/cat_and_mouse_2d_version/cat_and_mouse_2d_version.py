def cat_mouse(map_, moves):
    rows = map_.split('\n')
    c = next(((r, i) for r, row in enumerate(rows) for i, x in enumerate(row) if x == 'C'), None)
    m = next(((r, i) for r, row in enumerate(rows) for i, x in enumerate(row) if x == 'm'), None)
    if not c or not m:
        return "boring without two animals"
    return "Caught!" if abs(c[0] - m[0]) + abs(c[1] - m[1]) <= moves else "Escaped!"
