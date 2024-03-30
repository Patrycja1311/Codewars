def solve(a, b):
    unique_chars = set(a) ^ set(b)
    return ''.join(char for char in a + b if char in unique_chars)
