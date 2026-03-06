def hot_singles(arr1, arr2):
    return [x for x in dict.fromkeys(arr1+arr2) if (x in arr1) ^ (x in arr2)]
