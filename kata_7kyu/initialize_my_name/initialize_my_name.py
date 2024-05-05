def initialize_names(name):
    names = name.split()
    if len(names) > 2:
        for i in range(1, len(names) - 1):
            names[i] = names[i][0] + '.'
    return ' '.join(names)
