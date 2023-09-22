def row_weights(array):
    team_1 = sum(array[0::2])
    team_2 = sum(array[1::2])
    return team_1, team_2
