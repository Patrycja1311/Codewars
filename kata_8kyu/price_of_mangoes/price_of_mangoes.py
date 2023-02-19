def mango_1(quantity, price):
    sum_1 = (quantity // 3) * 2 * price
    sum_2 = (quantity % 3) * price
    return print(sum_1 + sum_2)


def mango_2(quantity, price):
    return print((((quantity // 3) * 2) + (quantity % 3)) * price)


if __name__ == '__main__':
    mango_1(3, 3)
    mango_1(9, 5)
    mango_2(3, 3)
    mango_2(9, 5)