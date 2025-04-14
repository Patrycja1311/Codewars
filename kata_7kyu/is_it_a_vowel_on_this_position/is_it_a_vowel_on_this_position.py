def check_vowel(strng, position):
    return position >= 0 and position < len(strng) and strng[position].lower() in 'aeiou'
