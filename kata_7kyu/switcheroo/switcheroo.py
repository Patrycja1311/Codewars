def switcheroo(s):
    dict_new = {'a':'b', 'b':'a'}
    return ''.join([dict_new.get(letter, 'c') for letter in s])
