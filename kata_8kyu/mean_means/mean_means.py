def geo_mean(nums, arith_mean):
    n = len(nums) + 1
    return (eval('*'.join(map(str, nums))) * (n * arith_mean - sum(nums))) ** (1 / n)
