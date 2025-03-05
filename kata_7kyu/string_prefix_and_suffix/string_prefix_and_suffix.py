def solve(st):
    return next((l for l in range(len(st) // 2, 0, -1) if st[:l] == st[-l:]), 0)
