def int_diff(lst, n):
    return sum(1 for i in range(len(lst)) for j in range(i + 1, len(lst)) if abs(lst[i] - lst[j]) == n)
