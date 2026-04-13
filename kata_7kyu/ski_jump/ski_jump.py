def ski_jump(mountain):
    h = len(mountain)
    j = round(1.35 * h * h, 2)
    return f"{j:.2f} metres: " + (
        "He's crap!" if j < 10 else
        "He's ok!" if j < 25 else
        "He's flying!" if j < 50 else
        "Gold!!"
    )
