def replace_all(obj, find, replace):
    if isinstance(obj, str):
        return obj.replace(find, replace)
    elif isinstance(obj, list):
        return [replace if item == find else item for item in obj]
    else:
        raise TypeError("replace_all supports only strings and lists")
