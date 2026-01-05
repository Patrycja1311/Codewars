def passed(lst):
    p = [x for x in lst if x <= 18]
    return round(sum(p) / len(p)) if p else 'No pass scores registered.'
