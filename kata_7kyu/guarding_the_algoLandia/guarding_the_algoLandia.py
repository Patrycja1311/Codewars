def find_needed_guards(k):
    n = 0
    for i in range(len(k) - 1):
        if not k[i] and not k[i + 1]:
            k[i + 1] = True
            n += 1
    return n

