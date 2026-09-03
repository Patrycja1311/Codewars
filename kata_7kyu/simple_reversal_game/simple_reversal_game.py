def solve(n, k):
    return min(2 * k + 1, n - 1) if k < n / 2 else 2 * (n - 1 - k)
