def compose(s1, s2):
    l1, l2 = s1.split('\n'), s2.split('\n')
    n = len(l1)
    return '\n'.join(l1[i][:i+1] + l2[-1-i][:n-i] for i in range(n))
