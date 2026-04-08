def sort_by_height(a):
    people = sorted([x for x in a if x != -1])
    result = []
    i = 0
    for x in a:
        if x == -1:
            result.append(-1)
        else:
            result.append(people[i])
            i += 1
    return result
