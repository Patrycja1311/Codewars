import random


def find_random_seed(target):
    for seed in range(10000):
        random.seed(seed)
        if [random.randint(0, 100) for _ in range(10)] == target:
            return seed
