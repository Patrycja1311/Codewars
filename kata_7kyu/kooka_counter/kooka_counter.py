def kooka_counter(laughing):
    groups = []
    i = 0
    while i < len(laughing):
        if laughing[i:i+2] == "Ha":
            groups.append("Ha")
            i += 2
        elif laughing[i:i+2] == "ha":
            groups.append("ha")
            i += 2
        else:
            i += 1
    return sum(groups[i] != groups[i-1] for i in range(1, len(groups))) + 1 if groups else 0
