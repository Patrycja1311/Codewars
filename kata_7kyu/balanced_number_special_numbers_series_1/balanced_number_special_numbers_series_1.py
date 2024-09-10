def balanced_num(number):
    s = str(number)
    n = len(s)
    left_sum = sum(map(int, s[:n//2 - (n % 2 == 0)]))
    right_sum = sum(map(int, s[n//2 + 1:]))
    return "Balanced" if left_sum == right_sum else "Not Balanced"
