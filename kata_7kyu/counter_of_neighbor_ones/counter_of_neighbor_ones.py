def ones_counter(inp):
    return [len(x) for x in ''.join(map(str, inp)).split('0') if x]
