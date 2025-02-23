import math


def strong_enough(earthquake, age):
    strength = 1000 * math.exp(-0.01 * age)
    magnitude = math.prod(sum(shockwave) for shockwave in earthquake)
    return "Safe!" if strength >= magnitude else "Needs Reinforcement!"
