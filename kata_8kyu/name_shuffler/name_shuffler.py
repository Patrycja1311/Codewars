def name_shuffler(str_):
    word = str_.split()
    return ' '.join([word[-1]] + word[1:-1] + [word[0]]) if len(word) >= 2 else str_
