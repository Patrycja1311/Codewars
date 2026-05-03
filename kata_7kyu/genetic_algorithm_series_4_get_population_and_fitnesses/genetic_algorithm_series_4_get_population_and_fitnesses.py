def map_population_fit(population, fitness):
    return [ChromosomeWrap(chromosome=p, fitness=fitness(p)) for p in population]
