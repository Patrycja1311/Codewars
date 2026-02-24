def how_much_coffee(events):
    valid = {"cw", "dog", "cat", "movie"}
    coffee = sum(
        1 if e.islower() else 2
        for e in events
        if e.lower() in valid
    )
    return coffee if coffee <= 3 else "You need extra sleep"
