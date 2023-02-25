def sum_no_duplicates(l):
    new_set = set()
    for i in l:
        new_set.add(i)
        if l.count(i) > 1:
            new_set.remove(i)
    return sum(new_set)


if __name__ == '__main__':
    sum_no_duplicates([1, 1, 2, 3])
    sum_no_duplicates([1, 1, 2, 2, 3])
    sum_no_duplicates([])
    sum_no_duplicates([1, 9, 9, 5, 7, 7, 6, 1, 5, 6])