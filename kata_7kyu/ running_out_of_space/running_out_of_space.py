def spacey(array):
    return [''.join(array[0:num+1]) for num, word in enumerate(array)]
