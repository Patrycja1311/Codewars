def sum_factorial(lst):
    def factorial(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    return sum(factorial(num) for num in lst)
