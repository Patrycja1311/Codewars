def mean_vs_median(numbers):
    mean = sum(numbers) / len(numbers)
    median = sorted(numbers)[len(numbers) // 2]
    return 'mean' if mean > median else 'median' if median > mean else 'same'
