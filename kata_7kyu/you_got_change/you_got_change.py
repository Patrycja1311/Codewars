def give_change(amount):
    res = []
    for b in [100, 50, 20, 10, 5, 1]:
        res.append(amount // b)
        amount %= b
    return tuple(res[::-1])
