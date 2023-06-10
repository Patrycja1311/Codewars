def integrate(coefficient, exponent):
    new_coefficient = coefficient // (exponent + 1)
    new_exponent = exponent + 1
    return f'{new_coefficient}x^{new_exponent}'
