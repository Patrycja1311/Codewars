def array_leaders(numbers):
    leaders, right_sum = [], 0
    for num in reversed(numbers):
        if num > right_sum:
            leaders.append(num)
        right_sum += num
    return leaders[::-1]
