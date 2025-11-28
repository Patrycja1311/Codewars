def reverse_it(data):
    if isinstance(data, str):
        return data[::-1]
    if isinstance(data, bool):
        return data
    if isinstance(data, (int, float)):
        s = str(data)[::-1]
        return float(s) if '.' in s else int(s)
    return data
