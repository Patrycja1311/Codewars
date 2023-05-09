def to_acronym(inp):
    inp_split = inp.split(' ')
    return ''.join([word[:1] for word in inp_split]).upper()
