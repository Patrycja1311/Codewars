def find_lowest_int(k):
    n = 1
    while True:
        a = n * k
        b = a + n
        if sorted(str(a)) == sorted(str(b)):
            return n
        n += 1
