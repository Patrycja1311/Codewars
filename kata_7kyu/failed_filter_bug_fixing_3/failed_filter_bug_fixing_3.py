def filter_numbers(string):
    return ''.join(c for c in string if not c.isdigit())
