def factory(x):
    def multiplier(arr):
        return [x * n for n in arr]
    return multiplier
