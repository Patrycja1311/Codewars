def sum_digits(number):
    return sum([abs(int(digit)) for digit in str(number)if digit != '-'])
