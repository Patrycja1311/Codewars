def insert_dash2(num):
    num_str = str(num)
    result = [num_str[0]]

    for i in range(1, len(num_str)):
        prev, curr = num_str[i - 1], num_str[i]

        if prev != '0' and curr != '0':
            if int(prev) % 2 == 1 and int(curr) % 2 == 1:  # Both odd
                result.append('-')
            elif int(prev) % 2 == 0 and int(curr) % 2 == 0:  # Both even (nonzero)
                result.append('*')

        result.append(curr)

    return ''.join(result)
