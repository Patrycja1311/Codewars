def cartesian_neighbor(x, y):
    neighbors = [(x + dx, y + dy)
                 for dx in (-1, 0, 1)
                 for dy in (-1, 0, 1)
                 if not (dx == 0 and dy == 0)]
    return neighbors
