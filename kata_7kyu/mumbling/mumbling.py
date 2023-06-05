def accum(s):
    new_word = []
    for letter in range(len(s)):
        new_word.append((s[letter] * (letter + 1)).capitalize())
    return '-'.join(new_word)
