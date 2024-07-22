def remove_vowels(strng):
    return ''.join(char for char in strng if char.lower() not in 'aeiou')
