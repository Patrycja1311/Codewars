def bubblesort_once(l):
    result = l[:]
    for i in range(len(result) - 1):
        if result[i] > result[i + 1]:
            result[i], result[i + 1] = result[i + 1], result[i]
    return result
