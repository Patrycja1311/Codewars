def points(games):
    score = 0
    for i in games:
        if int(i[0]) > int(i[2]):
            score += 3
        elif int(i[0]) < int(i[2]):
            score += 0
        else:
            score += 1
    return score
