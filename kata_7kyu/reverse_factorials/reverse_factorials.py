def reverse_factorial(num):
    i, f = 1, 1
    while f < num:
        i += 1
        f *= i
    return f"{i}!" if f == num else "None"
