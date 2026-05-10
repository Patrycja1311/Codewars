def set_reducer(inp):
    while len(inp) > 1:
        result = []
        count = 1
        for i in range(1, len(inp)):
            if inp[i] == inp[i - 1]:
                count += 1
            else:
                result.append(count)
                count = 1
        result.append(count)
        inp = result
    return inp[0]
