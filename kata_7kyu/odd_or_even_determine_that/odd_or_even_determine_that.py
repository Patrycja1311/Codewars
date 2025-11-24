def odd_or_even(n):
    if n % 2 == 1:
        return "Either"
    return "Odd" if (n // 2) % 2 == 1 else "Even"
