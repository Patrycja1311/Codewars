def owned_cat_and_dog(cat_years, dog_years):
    f = lambda y, a: 0 if y < 15 else 1 if y < 24 else 2 + (y - 24) // a
    return [f(cat_years, 4), f(dog_years, 5)]
