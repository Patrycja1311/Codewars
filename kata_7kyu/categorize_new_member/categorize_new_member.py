def open_or_senior(data):
    result = ['Senior' if i[0] >= 55 and i[1] >= 7 else 'Open' for i in data]
    return result
