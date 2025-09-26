def compound_array(a, b):
    return [x for pair in zip(a, b) for x in pair] + a[len(b):] + b[len(a):]
