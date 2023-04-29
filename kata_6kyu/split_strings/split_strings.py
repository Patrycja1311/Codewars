def solution(s):
    if len(s) % 2 == 0:
        return [s[i:i+2] for i in range(0, len(s), 2)]
    else:
        return [s[i:i+2] for i in range(0, len(s) - 1, 2)] + [s[-1] + '_']
