def sing():
    result = []
    for n in range(99, 0, -1):
        bottle = "bottle" if n == 1 else "bottles"
        next_n = n - 1
        if next_n == 0:
            next_bottle = "no more bottles"
        elif next_n == 1:
            next_bottle = "1 bottle"
        else:
            next_bottle = f"{next_n} bottles"
        result.append(f"{n} {bottle} of beer on the wall, {n} {bottle} of beer.")
        result.append(f"Take one down and pass it around, {next_bottle} of beer on the wall.")
    result.append("No more bottles of beer on the wall, no more bottles of beer.")
    result.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
    return result
