def sort_transform(arr):
    f = lambda x: ''.join(map(chr, (x[0], x[1], x[-2], x[-1])))
    alpha = sorted(map(chr, arr))
    return '-'.join((
        f(arr),
        f(sorted(arr)),
        f(sorted(arr, reverse=True)),
        alpha[0] + alpha[1] + alpha[-2] + alpha[-1]
    ))
