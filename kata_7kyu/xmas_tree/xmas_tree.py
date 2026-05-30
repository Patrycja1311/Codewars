def xmastree(n):
    w = 2*n - 1
    tree = []
    for i in range(1, n+1):
        s = '#' * (2*i - 1)
        tree.append(s.center(w, '_'))
    trunk = '_' * (n-1) + '#' + '_' * (n-1)
    tree += [trunk, trunk]
    return tree
