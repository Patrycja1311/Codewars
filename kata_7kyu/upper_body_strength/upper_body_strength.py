def alex_mistakes(number_of_katas, time_limit):
    t = time_limit - number_of_katas * 6
    m, p = 0, 5
    while t >= p:
        t -= p
        p *= 2
        m += 1
    return m

