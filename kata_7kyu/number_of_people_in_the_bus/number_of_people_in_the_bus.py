def number(bus_stops):
    return max(0, sum(on - off for on, off in bus_stops))
