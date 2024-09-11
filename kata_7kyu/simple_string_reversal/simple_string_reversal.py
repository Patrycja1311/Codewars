def solve(s):
    chars = [c for c in s if c != ' '][::-1]
    return ''.join(chars.pop(0) if c != ' ' else ' ' for c in s)
