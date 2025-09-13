def say_me_operations(string_numbers):
    n=list(map(int, string_numbers.split()))
    return ", ".join(
        "addition" if a+b == c else
        "subtraction" if a-b == c else
        "multiplication" if a*b == c else
        "division"
        for a, b, c in zip(n, n[1:], n[2:])
    )
