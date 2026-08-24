def each_char(string, arg):
    if callable(arg):
        return ''.join(arg(c) for c in string)
    return ''.join(c + arg for c in string)
