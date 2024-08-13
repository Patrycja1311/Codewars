def insert_dash(num):
    return ''.join(a + ('-' if int(a) % 2 and int(b) % 2 else '') for a, b in zip(str(num), str(num)[1:])) + str(num)[-1]
