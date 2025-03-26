def cost(mins):
    if mins <= 65:
        return 30
    return 30 + ((mins - 65 + 29) // 30) * 10
