def vowel_2_index(string):
    return ''.join(str(i + 1) if char.lower() in 'aeiou' else char for i, char in enumerate(string))
