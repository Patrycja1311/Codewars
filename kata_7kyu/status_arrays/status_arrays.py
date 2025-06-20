def status(nums):
    return [v for _, _, v in sorted((i + sum(x < v for x in nums), i, v) for i, v in enumerate(nums))]
