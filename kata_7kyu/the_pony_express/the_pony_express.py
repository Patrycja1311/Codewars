def riders(stations):
    total_riders = 1
    current_distance = 0
    for distance in stations:
        if current_distance + distance > 100:
            total_riders += 1
            current_distance = distance
        else:
            current_distance += distance
    return total_riders
