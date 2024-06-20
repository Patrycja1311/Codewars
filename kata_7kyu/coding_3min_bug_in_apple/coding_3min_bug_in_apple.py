def sc(apple):
    return next([x, row.index('B')] for x, row in enumerate(apple) if 'B' in row)
