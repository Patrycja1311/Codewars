def digital_root(n):
    n_string = str(n)
    digit_sum = sum(int(digit) for digit in n_string)
    if digit_sum >= 10:
        return digital_root(digit_sum)
    else:
        return digit_sum
