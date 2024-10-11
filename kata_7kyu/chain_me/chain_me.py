def chain(init_val, functions):
    for func in functions:
        init_val = func(init_val)
    return init_val
