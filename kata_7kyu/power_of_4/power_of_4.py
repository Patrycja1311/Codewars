def powerof4(n):
    return (
        type(n) is int and
        n > 0 and
        n & (n - 1) == 0 and
        n % 3 == 1
    )
