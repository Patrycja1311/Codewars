def last_survivor(letters, coords):
    letters = list(letters)
    for index in coords:
        del letters[index]
    return letters[0]
