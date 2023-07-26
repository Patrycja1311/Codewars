def lineup_students(string):
    sorted_names = sorted(string.split(), key=lambda name: (len(name), name), reverse=True)
    return sorted_names
