def kaprekar_split(n):
    s = str(n*n)
    for i in range(len(s)+1):
        if int(s[:i] or 0) + int(s[i:] or 0) == n:
            return i
    return -1
