def process_2arrays(arr1, arr2):
    s1 = set(arr1)
    s2 = set(arr2)
    both = len(s1 & s2)
    only_one = len(s1 ^ s2)
    remaining1 = len(s1 - s2)
    remaining2 = len(s2 - s1)
    return [both, only_one, remaining1, remaining2]
