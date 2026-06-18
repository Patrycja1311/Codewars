def infected(s):
    population = sum(c in '01' for c in s)
    if population == 0:
        return 0
    infected_population = 0
    for continent in s.split('X'):
        if '1' in continent:
            infected_population += len(continent)
    return infected_population * 100 / population
