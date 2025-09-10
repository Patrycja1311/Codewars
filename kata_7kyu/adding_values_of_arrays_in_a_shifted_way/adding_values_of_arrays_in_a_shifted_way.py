def sum_arrays(arrays, shift):
    res = []
    for i, arr in enumerate(arrays):
        pos = i * shift
        res += [0] * max(0, pos + len(arr) - len(res))
        res[pos:pos+len(arr)] = [a+b for a, b in zip(res[pos:pos+len(arr)], arr)]
    return res
