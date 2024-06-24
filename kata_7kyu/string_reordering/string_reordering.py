def sentence(lst):
    return ' '.join(v for k, v in sorted((int(k), v) for d in lst for k, v in d.items()))
