def create_dict(keys, values):
    result = {}
    for i in range(len(keys)):
        if i < len(values):
            result[keys[i]] = values[i]
        else:
            result[keys[i]] = None
    return result
