def evil(n):
    count_one = bin(n).count('1')
    return "It's Evil!" if count_one % 2 == 0 else "It's Odious!"
