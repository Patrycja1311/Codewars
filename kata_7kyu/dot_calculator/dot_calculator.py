def calculator(txt):
    num1, operator, num2 = txt.split()
    num1, num2 = len(num1), len(num2)

    result = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '//': num1 // num2
    }[operator]

    return '.' * result
