def vowel_indices(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return [i + 1 for i, letter in enumerate(word.lower()) if letter in vowels]
