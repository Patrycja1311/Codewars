from functools import reduce


def count_zeros_n_double_fact(n):
    even_list = []
    odd_list = []
    if n % 2 == 0:
        for i in range(2, n+1, 2):
           even_list.append(i)
    else:
        for i in range(1, n+1, 2):
            odd_list.append(i)
    if len(even_list) > 0:
        number = reduce(lambda x, y: x*y, even_list)
    elif len(odd_list) > 0:
        number = reduce(lambda x, y: x*y, odd_list)

    len_number = len(str(number))

    list_n = []
    for n in range(len_number):
        if number % 10 ** n == 0:
            list_n.append(n)

    return print(list_n[-1])


count_zeros_n_double_fact(30)


