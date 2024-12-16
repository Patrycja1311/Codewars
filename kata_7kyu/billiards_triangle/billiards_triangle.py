def pyramid(balls):
    levels = 0
    while balls > levels:
        levels += 1
        balls -= levels
    return levels
