def is_same_language(lst):
    return len(set(dev['language'] for dev in lst)) == 1
