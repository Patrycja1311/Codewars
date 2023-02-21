def add_length_2(str_):
    x = [f'{i} {len(i)}' for i in str_.split(' ')]
    return print(x)


if __name__ == '__main__':
    add_length_2("you will win")