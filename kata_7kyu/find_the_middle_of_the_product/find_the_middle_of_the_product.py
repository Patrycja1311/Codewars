def find_middle(st):
    if not isinstance(st, str):
        return -1

    digits = [int(c) for c in st if c.isdigit()]

    if not digits:
        return -1

    product = 1
    for d in digits:
        product *= d

    result = str(product)
    mid = len(result) // 2

    if len(result) % 2 == 0:
        return int(result[mid - 1:mid + 1])
    else:
        return int(result[mid])

