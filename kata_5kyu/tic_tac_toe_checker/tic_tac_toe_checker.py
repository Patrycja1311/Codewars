def is_solved(board):
    n = 0

    for row in board:
        # check horizontally
        if row[0] == row[1] == row[2] and row[0] != 0:
            return row[0]

        # check perpendicularly
        elif board[0][n] == board[1][n] == board[2][n] and board[0][n] != 0:
            win = board[0][n]
            return win
        n += 1

    # check diagonal
    if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]) and board[1][1] != 0:
        return board[1][1]

    list_zero = []
    for element in board:
        for item in element:
            # check not yet finished AND no one won
            if item == 0:
                list_zero.append(item)

    if len(list_zero) >= 1:
        return -1

    # check cat's game
    if len(list_zero) == 0:
        return 0