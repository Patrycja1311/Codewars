def narcissistic(value):
    new_n = [int(digit) for digit in str(value)]
    sum_n = sum([digit **len(new_n) for digit in new_n])
    return value == sum_n
