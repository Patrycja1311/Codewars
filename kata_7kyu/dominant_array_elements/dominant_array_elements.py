def solve(arr):
    dominant = [arr[-1]]
    for x in reversed(arr[:-1]):
        if x > dominant[-1]:
            dominant.append(x)
    return dominant[::-1]
