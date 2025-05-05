def cyclops(n):
    b = bin(n)[2:]
    return b[len(b)//2] == '0' and b.count('0') == 1 and len(b)%2
