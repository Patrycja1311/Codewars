def barista(coffees):
    total = time = 0
    for i, c in enumerate(sorted(coffees)):
        time += c
        total += time
        if i < len(coffees)-1:
            time += 2
    return total
