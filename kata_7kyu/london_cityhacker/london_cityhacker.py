def london_city_hacker(journey):
    total, buses = 0, 0
    for x in journey + [None]:
        if isinstance(x, int):
            buses += 1
        else:
            total += ((buses + 1) // 2) * 1.5
            buses = 0
            if isinstance(x, str):
                total += 2.4
    return f"£{total:.2f}"
