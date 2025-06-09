def strange_math(n, k):
    sorted_nums = sorted(map(str, range(1, n + 1)))
    return sorted_nums.index(str(k)) + 1
