def tower_builder(n_floors):
    tower = []
    for i in range(1, n_floors + 1):
        left_padding = ' ' * (n_floors - i)
        top = '*' * (2 * i - 1)
        right_padding = ' ' * (n_floors - i)
        floor = left_padding + top + right_padding
        tower.append(floor)
    return tower
