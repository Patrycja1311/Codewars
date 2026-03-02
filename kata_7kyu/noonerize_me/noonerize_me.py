def noonerize(numbers):
    if not all(isinstance(x, int) for x in numbers):
        return "invalid array"
    a, b = map(str, numbers)
    return abs(int(b[0] + a[1:]) - int(a[0] + b[1:]))
