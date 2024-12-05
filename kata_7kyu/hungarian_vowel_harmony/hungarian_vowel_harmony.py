def dative(word):
    front_vowels = "eéiíöőüű"
    back_vowels = "aáoóuú"
    last_vowel = next((char for char in reversed(word) if char in front_vowels + back_vowels), None)
    return word + ("nek" if last_vowel in front_vowels else "nak")
