def single_digit(n):
    while n >= 10:
        binary = bin(n)[2:]
        n = sum(int(digit) for digit in binary)
    return n
