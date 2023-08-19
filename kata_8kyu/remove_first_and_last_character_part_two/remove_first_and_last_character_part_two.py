def array(string):
    list_str = string.split(',')
    new_str = list_str[1:-1]
    return None if len(new_str) < 1 else ' '.join(new_str)
