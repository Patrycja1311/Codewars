def brightest(colors):
    return max(
        colors,
        key=lambda c: max(int(c[i:i + 2], 16) for i in (1, 3, 5))
    )
