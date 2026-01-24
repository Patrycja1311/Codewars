def example_sort(arr, example_arr):
    order = {v: i for i, v in enumerate(example_arr)}
    return sorted(arr, key=lambda x: order[x])
