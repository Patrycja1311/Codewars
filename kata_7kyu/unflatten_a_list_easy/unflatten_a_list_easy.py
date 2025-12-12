def unflatten(flat_array):
    res, i = [], 0
    while i < len(flat_array):
        x = flat_array[i]
        if x < 3:
            res.append(x)
            i += 1
        else:
            res.append(flat_array[i:i+x])
            i += x
    return res
