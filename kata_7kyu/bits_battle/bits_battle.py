def bits_battle(numbers):
    o = sum(bin(n).count("1") for n in numbers if n % 2)
    e = sum(bin(n)[2:].count("0") for n in numbers if n and n % 2 == 0)
    return "odds win" if o > e else "evens win" if o < e else "tie"
