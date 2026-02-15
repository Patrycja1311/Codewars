def validate_ean(code):
    digits = [int(d) for d in code]
    total = 0
    for i in range(12):
        if i % 2 == 0:
            total += digits[i] * 1
        else:
            total += digits[i] * 3
    if total % 10 == 0:
        checksum = 0
    else:
        checksum = 10 - (total % 10)
    return checksum == digits[12]
