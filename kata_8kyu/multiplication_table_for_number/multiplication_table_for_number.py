def multi_table(number):
    z = str()
    for x in range(1, 11):
        multi = x * number
        z += f'{x} * {number} = {multi}\n'
    y = z.strip('\n')
    return y
