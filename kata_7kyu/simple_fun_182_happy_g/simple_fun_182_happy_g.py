def happy_g(st):
    return all(
        ch != 'g' or
        (i > 0 and st[i-1] == 'g') or
        (i < len(st)-1 and st[i+1] == 'g')
        for i, ch in enumerate(st)
    )
