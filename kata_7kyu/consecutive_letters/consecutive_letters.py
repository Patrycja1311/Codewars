def solve(st):
    return len(st) == len(set(st)) and ord(max(st)) - ord(min(st)) == len(st) - 1
