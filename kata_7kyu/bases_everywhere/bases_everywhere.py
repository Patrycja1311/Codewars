def base_finder(seq):
    unique_digits = set()
    for number in seq:
        for digit in number:
            unique_digits.add(digit)
    return len(unique_digits)
