def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def strong_num(number):
    return "STRONG!!!!" if sum(factorial(int(d)) for d in str(number)) == number else "Not Strong !!"
