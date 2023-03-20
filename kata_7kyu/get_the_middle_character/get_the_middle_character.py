def get_middle(s):
    d = int(len(s))
    if d % 2 == 0:
        n = int(d/2)
        return s[n-1:n+1]
    else:
        k = int(d/2)
        return s[k]