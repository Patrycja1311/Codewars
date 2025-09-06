def filter_homogenous(arrays):
    result = []
    for sub in arrays:
        if sub:  # ignore empty arrays
            first_type = type(sub[0])   # take the type of the first element
            if all(isinstance(x, first_type) for x in sub):  # check all same type
                result.append(sub)
    return result
