def find_spaceship(astromap):
    rows = astromap.split('\n')
    for i, row in enumerate(rows):
        if 'X' in row:
            return [row.index('X'), len(rows) - 1 - i]
    return "Spaceship lost forever."
