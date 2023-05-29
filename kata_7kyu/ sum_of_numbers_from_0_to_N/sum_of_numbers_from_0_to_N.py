def show_sequence(n):
    if n > 0:
        numbers = [num for num in range(n + 1)]
        total = sum(numbers)
        str_numbers = '+'.join(str(num) for num in numbers)
        return f'{str_numbers} = {total}'
    elif n == 0:
        return f'0=0'
    else:
        return f'{n}<0'
