def stone_pick(arr):
    sticks = sum(4 if material == "Wood" else 1 for material in arr if material in ["Sticks", "Wood"])
    stones = arr.count("Cobblestone")
    return min(sticks // 2, stones // 3)
