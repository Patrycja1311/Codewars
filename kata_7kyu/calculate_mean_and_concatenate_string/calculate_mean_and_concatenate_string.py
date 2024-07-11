def mean(lst):
    integers = [int(x) for x in lst if x.isdigit()]
    characters = ''.join(x for x in lst if not x.isdigit())
    return [sum(integers) / len(integers), characters]
