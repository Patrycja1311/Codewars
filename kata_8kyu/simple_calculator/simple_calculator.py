def calculator(x, y, op):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            return x / y
        else:
            return "unknown value"
    else:
        return "unknown value"
