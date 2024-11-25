def snail(column, day, night):
    return 1 if day >= column else (column - day + (day - night) - 1) // (day - night) + 1
