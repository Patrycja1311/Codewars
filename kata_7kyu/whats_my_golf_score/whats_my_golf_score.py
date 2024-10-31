def golf_score_calculator(par_string, score_string):
    return sum(int(stroke) - int(p) for p, stroke in zip(par_string, score_string))
