def vert_mirror(strng):
    return '\n'.join(line[::-1] for line in strng.split('\n'))


def hor_mirror(strng):
    return '\n'.join(strng.split('\n')[::-1])


def oper(fct, s):
    return fct(s)