def i(word):
    v = sum(c in "aeiouAEIOU" for c in word)
    c = sum(c.isalpha() and c not in "aeiouAEIOU" for c in word)
    return "i"+word if word and word[0].isupper() and not word.startswith("I") and v < c else "Invalid word"
