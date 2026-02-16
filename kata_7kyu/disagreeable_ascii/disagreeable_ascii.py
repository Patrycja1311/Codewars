def get_weight(name):
    total = 0
    for ch in name:
        if ch.isalpha():
            if ch.islower():
                total += ord(ch.upper())
            else:
                total += ord(ch.lower())
    return total
