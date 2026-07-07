def make_lazy(*args):
    return lambda: args[0](*args[1:])
