def odd_one(arr):
    return next((i for i, num in enumerate(arr) if num % 2 != 0), -1)
