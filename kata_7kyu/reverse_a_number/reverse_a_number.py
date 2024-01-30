def reverse_number(n):
    if n == 0:
        return 0
    multi = -1 if n < 0 else 1
    number = n if n > 0 else n * (-1)
    return int(''.join([num for num in str(number)])[::-1]) * multi
