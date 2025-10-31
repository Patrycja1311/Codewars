def burner(c, h, o):
    water = min(h//2, o); h -= 2*water; o -= water
    co2 = min(c, o//2); c -= co2; o -= 2*co2
    methane = min(c, h//4)
    return water, co2, methane
