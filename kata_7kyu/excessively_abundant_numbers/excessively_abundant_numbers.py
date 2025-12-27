def abundant_number(num):
    return num > 11 and sum(i for i in range(1, num) if num % i == 0) > num
