def find_outlier(integers):
    odd = [x for x in integers if x % 2]
    even = [x for x in integers if x % 2 == 0]
    return odd[0] if len(odd) == 1 else even[0]
