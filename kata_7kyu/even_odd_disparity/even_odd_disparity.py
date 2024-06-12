def solve(a):
    evens = sum(1 for x in a if isinstance(x, int) and x % 2 == 0)
    odds = sum(1 for x in a if isinstance(x, int) and x % 2 != 0)
    return evens - odds
