def two_sum(numbers, target):
    index_dict = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in index_dict:
            return (index_dict[complement], i)
        index_dict[num] = i
    return None
