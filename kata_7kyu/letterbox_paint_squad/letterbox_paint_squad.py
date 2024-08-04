def paint_letterboxes(start, finish):
    return [sum(str(i).count(str(d)) for i in range(start, finish + 1)) for d in range(10)]
