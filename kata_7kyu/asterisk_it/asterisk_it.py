def asterisc_it(n):
    s = ''.join(map(str, n)) if isinstance(n, (list, tuple)) else str(n)
    return ''.join(
        s[i] + ('*' if i < len(s)-1 and int(s[i]) % 2 == 0 and int(s[i+1]) % 2 == 0 else '')
        for i in range(len(s))
    )
