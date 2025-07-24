def calculate(strng):
    a, b = [int(w) for w in strng.split() if w.isdigit()]
    return a + b if 'gains' in strng else a - b
