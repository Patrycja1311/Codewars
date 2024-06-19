def absent_vowel(x):
    return next(i for i, vowel in enumerate('aeiou') if vowel not in x)
