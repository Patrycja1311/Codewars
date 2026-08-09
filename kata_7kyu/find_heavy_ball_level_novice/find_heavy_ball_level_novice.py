def find_ball(scales):
    w = scales.get_weight([0, 1, 2], [3, 4, 5])

    if w == -1:
        w = scales.get_weight([0], [1])
        if w == -1:
            return 0
        elif w == 1:
            return 1
        else:
            return 2

    elif w == 1:
        w = scales.get_weight([3], [4])
        if w == -1:
            return 3
        elif w == 1:
            return 4
        else:
            return 5

    else:
        w = scales.get_weight([6], [7])
        if w == -1:
            return 6
        else:
            return 7
