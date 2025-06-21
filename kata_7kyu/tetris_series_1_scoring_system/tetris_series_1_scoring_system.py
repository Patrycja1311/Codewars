def get_score(arr) -> int:
    score = total = 0
    for x in arr:
        lvl = total // 10
        score += (40 if x == 1 else 100 if x == 2 else 300 if x == 3 else 1200 if x == 4 else 0) * (lvl + 1)
        total += x
    return score
