def check_exam(arr1, arr2):
    return max(sum(4 if a2 == a1 else -1 for a2, a1 in zip(arr2, arr1) if a2 != ""), 0)
