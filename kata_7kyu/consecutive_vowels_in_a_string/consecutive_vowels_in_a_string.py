def get_the_vowels(word):
    v, i, c = 'aeiou', 0, 0
    for ch in word:
        if ch == v[i]:
            c += 1
            i = (i + 1) % 5
    return c
