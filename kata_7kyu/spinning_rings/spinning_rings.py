def spinning_rings(inner_max, outer_max):
    i, o, m = 0, 0, 0
    while True:
        m += 1
        i = (i - 1) % (inner_max + 1)
        o = (o + 1) % (outer_max + 1)
        if i == o:
            return m
