def is_lucky(n):
    digit_sum = sum(int(digit) for digit in str(n))
    return digit_sum == 0 or digit_sum % 9 == 0
