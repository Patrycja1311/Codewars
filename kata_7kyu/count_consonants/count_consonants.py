def consonant_count(s):
    return sum(1 for char in s if char.isalpha() and char.lower() not in "aeiou")
