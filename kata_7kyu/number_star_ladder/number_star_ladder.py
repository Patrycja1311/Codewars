def pattern(n):
    lines = ["1"]
    for i in range(2, n + 1):
        lines.append("1" + "*" * (i - 1) + str(i))
    return "\n".join(lines)
