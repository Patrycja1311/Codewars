def explode(arr):
    nums = [n for n in arr if isinstance(n, (int, float))]
    return [arr] * sum(nums) if nums else "Void!"
