def fibs_fizz_buzz(n):
    fib = [1, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return [
        "FizzBuzz" if x % 15 == 0 else
        "Fizz" if x % 3 == 0 else
        "Buzz" if x % 5 == 0 else x
        for x in fib[:n]
    ]
