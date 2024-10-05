def numbers_with_digit_inside(x, d):
    nums = [num for num in range(1, x + 1) if str(d) in str(num)]
    if not nums:
        return [0, 0, 0]
    return [len(nums), sum(nums), eval('*'.join(map(str, nums)))]
