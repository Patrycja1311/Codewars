def crazy_formula(n):
    while n >= 10:
        digits = list(map(int, str(n)))
        if len(digits) % 2 == 0:
            digits.pop()
        mid, last = len(digits) // 2, digits[-1]
        middle_digit = digits[mid]

        total = sum(digits)
        if middle_digit % 2 != 0:
            total -= 2 * middle_digit
        if middle_digit % 2 == 0 and last % 2 == 0:
            total -= 2 * last
        if middle_digit % 2 == 0 and last % 2 != 0:
            total += digits[0] ** 2 - digits[0]

        n = abs(total)
    return n
