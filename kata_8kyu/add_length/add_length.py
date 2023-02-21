new_list = []

def add_length_1(str_):
    new = str_.split(' ')
    for i in new:
        x = len(i)
        new_list.append(f'{i} {x}')
    return print(new_list)


if __name__ == '__main__':
    add_length_1("you will win")