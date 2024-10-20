def no_repeat(string):
    return next(char for char in string if string.count(char) == 1)
