def count_salutes(hallway):
    salutes = right = 0
    for c in hallway:
        if c == '>':
            right += 1
        elif c == '<':
            salutes += 2 * right
    return salutes
