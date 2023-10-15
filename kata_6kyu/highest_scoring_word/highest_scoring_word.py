import string


def high(x):
    alphabet = string.ascii_lowercase
    letter_points = {i: alphabet.index(i) + 1 for i in alphabet}
    results = [sum(letter_points[letter] for letter in word) for word in x.split()]
    return x.split()[results.index(max(results))]
