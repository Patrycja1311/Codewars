def solve(arr):
    seen = set()
    for num in arr:
        if -num in seen:
            seen.remove(-num)
        else:
            seen.add(num)
    return seen.pop()
