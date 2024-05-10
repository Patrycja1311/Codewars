def array_mash(a, b):
    merged = []
    for i in range(len(a)):
        merged.append(a[i])
        merged.append(b[i])
    return merged
