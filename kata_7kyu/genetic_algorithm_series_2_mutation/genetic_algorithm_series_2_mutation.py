import random


def mutate(chromosome, p):
    return ''.join(
        str(1 - int(gene)) if random.random() < p else gene
        for gene in chromosome
    )
