def correct(s):
    correct_dict = {'5': 'S', '0': 'O', '1': 'I'}
    return ''.join(correct_dict.get(i, i) for i in s)
