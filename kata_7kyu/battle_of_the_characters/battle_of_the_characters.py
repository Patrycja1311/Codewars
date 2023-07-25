def battle(x, y):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    x_power = sum([alphabet.index(x_index)+1 for x_index in [letter for letter in x]])
    y_power = sum([alphabet.index(y_index)+1 for y_index in [letter for letter in y]])
    if x_power > y_power:
        return x
    elif y_power > x_power:
        return y
    else:
        return 'Tie!'
