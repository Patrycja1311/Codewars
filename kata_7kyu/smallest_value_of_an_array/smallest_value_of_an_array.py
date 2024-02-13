def find_smallest(numbers, to_return):
    num = min(numbers)
    ind = numbers.index(num)
    return num if to_return == "value" else ind
