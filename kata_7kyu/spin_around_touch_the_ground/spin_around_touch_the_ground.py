def spin_around(lst):
    angle = 0
    for direction in lst:
        if direction == "right":
            angle += 90
        else:
            angle -= 90
    return abs(angle) // 360

