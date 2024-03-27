def calculate_value(s):
    value = sum(ord(c) - ord('a') + 1 for c in s if c.isalpha())
    return value


def name_value(my_list):
    result = []
    for i, s in enumerate(my_list, 1):
        result.append(calculate_value(s) * i)
    return result
