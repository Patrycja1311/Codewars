def count_duplicates(name, age, height):
    entries = list(zip(name, age, height))
    return len(entries) - len(set(entries))
