def sect_sort(a, start, length=0):
    end = None if not length else start + length
    a[start:end] = sorted(a[start:end])
    return a
