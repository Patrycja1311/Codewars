def connotation(strng):
    return sum(w[0].lower() <= 'm' for w in strng.split()) * 2 >= len(strng.split())
