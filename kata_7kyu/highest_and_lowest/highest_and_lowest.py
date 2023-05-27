def high_and_low(numbers):
    int_num = [int(num) for num in numbers.split()]
    return f'{max(int_num)} {min(int_num)}'
