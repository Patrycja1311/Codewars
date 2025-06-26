def grid_index(grid, indexes):
    n = len(grid)
    result = ''
    for i in indexes:
        row = (i - 1) // n
        col = (i - 1) % n
        result += grid[row][col]
    return result
