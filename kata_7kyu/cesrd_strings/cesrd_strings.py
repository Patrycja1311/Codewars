def uncensor(infected, discovered):
    it = iter(discovered)
    return ''.join(c if c != '*' else next(it) for c in infected)
