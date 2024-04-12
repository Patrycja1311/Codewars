def hydrate(drink_string):
    total_drinks = sum(int(word) for word in drink_string.split() if word.isdigit())
    return f"{total_drinks} {'glass' if total_drinks == 1 else 'glasses'} of water"
