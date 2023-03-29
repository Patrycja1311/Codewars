def array_diff(a, b):
    for i in a:
        for j in b:
            if j in a:
                a.remove(j)
    return a