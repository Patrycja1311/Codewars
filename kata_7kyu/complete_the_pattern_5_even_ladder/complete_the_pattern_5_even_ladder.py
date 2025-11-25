def pattern(n):
    if n <= 1:
        return ""
    if n % 2 == 1:
        n -= 1
    lines = []
    for i in range(2, n + 1, 2):
        lines.append(str(i) * i)
    return "\n".join(lines)
