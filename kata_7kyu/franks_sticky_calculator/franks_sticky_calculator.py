def sticky_calc(operation, val1, val2):
    val1 = round(val1)
    val2 = round(val2)
    stuck = int(str(val1) + str(val2))
    if operation == '+':
        result = stuck + val2
    elif operation == '-':
        result = stuck - val2
    elif operation == '*':
        result = stuck * val2
    elif operation == '/':
        result = stuck / val2
    else:
        raise ValueError("Niepoprawna operacja")
    return round(result)
