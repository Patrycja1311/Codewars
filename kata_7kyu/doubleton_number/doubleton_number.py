def doubleton(num):
    x = num + 1
    while True:
        if len(set(str(x))) == 2:
            return x
        x += 1
