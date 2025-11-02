def sort_by_value_and_index(arr):
    return [x for _, _, x in sorted((x*(i+1), i, x) for i, x in enumerate(arr))]
