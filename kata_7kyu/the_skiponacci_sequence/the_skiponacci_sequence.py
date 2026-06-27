def skiponacci(n):
    a, b = 1, 1
    result = []

    for i in range(1, n + 1):
        result.append(str(a) if i % 2 else "skip")
        a, b = b, a + b

    return " ".join(result)
