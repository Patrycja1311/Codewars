def reverse(a):
    s, i, res = ''.join(a)[::-1], 0, []
    for w in a:
        res.append(s[i:i+len(w)])
        i += len(w)
    return res
