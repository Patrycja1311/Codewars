def grid_map(inp, op):
    return [[op(element) for element in sublist] for sublist in inp]
