def expanded_form(num):
    new_num = []
    for i in range(1, len(str(num)) + 1):
        new_num.append(str(num % 10 ** i))
        num = num - num % 10 ** i
        if new_num[-1] == "0":
            new_num.pop()

    return " + ".join(new_num[::-1])
