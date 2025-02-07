def plant(seed, water, fert, temp):
    flower = seed * fert if 20 <= temp <= 30 else seed
    return (("-" * water) + flower) * water if 20 <= temp <= 30 else ("-" * water * water) + seed
