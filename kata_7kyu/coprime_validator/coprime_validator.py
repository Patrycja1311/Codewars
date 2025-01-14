def are_coprime(n, m):
    def find_gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    gcd = find_gcd(n, m)
    return gcd == 1
