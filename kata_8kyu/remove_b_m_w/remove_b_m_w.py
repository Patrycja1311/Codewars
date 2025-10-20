def remove_bmw(string):
    if not isinstance(string, str): raise TypeError("This program only works for text.")
    return ''.join(c for c in string if c not in 'BMWbmw')
