def parts_sums(ls):
    new_list = [sum(ls)]
    for i in ls:
        new_list.append(new_list[-1] - i)
    return new_list if ls else [0]
