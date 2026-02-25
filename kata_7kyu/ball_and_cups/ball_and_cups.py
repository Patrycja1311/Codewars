def cup_and_balls(b, arr):
    position = b
    for x, y in arr:
        if position == x:
            position = y
        elif position == y:
            position = x
    return position
