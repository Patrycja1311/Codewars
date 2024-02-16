def calculate(num1, operation, num2):
    operations = {"+": lambda x, y: x + y,
                  "-": lambda x, y: x - y,
                  "*": lambda x, y: x * y,
                  "/": lambda x, y: x / y if y != 0 else None}
    return operations.get(operation, lambda x, y: None)(num1, num2)
