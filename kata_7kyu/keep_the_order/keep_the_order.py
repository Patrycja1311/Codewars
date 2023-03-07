def keep_order(ary, val):
    ary.append(val)
    new_ary = sorted(ary)
    new_index = new_ary.index(val)
    return new_index


if __name__ == '__main__':
    keep_order([1, 2, 3, 4, 7], 5)