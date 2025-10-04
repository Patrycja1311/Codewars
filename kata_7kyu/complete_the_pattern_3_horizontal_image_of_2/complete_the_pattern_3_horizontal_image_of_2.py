def pattern(n):
    if n <= 0:
        return ""
    return "\n".join("".join(str(n - j) for j in range(i)) for i in range(1, n + 1))
