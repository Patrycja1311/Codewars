def fire(x, y):
    grid = ["top left", "top middle", "top right",
            "middle left", "center", "middle right",
            "bottom left", "bottom middle", "bottom right"]
    return grid[y * 3 + x]
