def score_to_tally(score):
    result = "e <br>" * (score // 5)
    rest = score % 5

    if rest:
        result += "abcde"[rest - 1]

    return result

