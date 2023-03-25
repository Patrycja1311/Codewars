def solution(number):
    return sum(set(num for num in range(number) if num % 3 == 0 or num % 5 == 0))
