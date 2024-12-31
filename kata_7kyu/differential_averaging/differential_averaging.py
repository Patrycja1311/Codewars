def add_to_average(current, points, add):
    new_average = (current * points + add) / (points + 1)
    return new_average
