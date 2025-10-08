def move_vowels(input):
    return ''.join([c for c in input if c not in 'aeiou'] + [c for c in input if c in 'aeiou'])
