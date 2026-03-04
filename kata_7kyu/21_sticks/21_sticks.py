def make_move(sticks):
    move = sticks % 4
    return move if move != 0 else 1
