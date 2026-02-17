def clonewars(kata_per_day):
    if kata_per_day == 0:
        clones = 1
    else:
        clones = 2 ** (kata_per_day - 1)
    if kata_per_day == 0:
        total_kata = 0
    else:
        total_kata = (2 ** (kata_per_day + 1)) - kata_per_day - 2
    return [clones, total_kata]
