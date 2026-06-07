def counter():
    i = 0
    def f():
        nonlocal i
        i += 1
        return i
    return f
