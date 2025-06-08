def distinct_digit_year(year):
    return next(x for x in range(year + 1, 10000) if len(set(str(x))) == 4)
