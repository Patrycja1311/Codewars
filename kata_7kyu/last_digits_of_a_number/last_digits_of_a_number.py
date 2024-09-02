def solution(n, d):
    return [int(digit) for digit in str(n)[-d:]] if d > 0 else []
