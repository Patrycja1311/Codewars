def solve(s):
    return max(len(v) for v in ''.join('v' if c in 'aeiou' else 'c' for c in s).split('c'))
