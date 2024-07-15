def flatten(lst):
    flattened = []
    for element in lst:
        if isinstance(element, list):
            flattened.extend(element)
        else:
            flattened.append(element)
    return flattened
