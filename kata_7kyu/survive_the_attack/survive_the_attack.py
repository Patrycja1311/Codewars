def is_defended(attackers, defenders):
    a_s = d_s = 0
    for a, d in zip(attackers + [0]*len(defenders), defenders + [0]*len(attackers)):
        if a > d: a_s += 1
        elif d > a: d_s += 1
    return d_s > a_s or (d_s == a_s and sum(defenders) >= sum(attackers))

