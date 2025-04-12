def tacofy(word):
    mapping = {
        'a': 'beef', 'e': 'beef', 'i': 'beef', 'o': 'beef', 'u': 'beef',
        't': 'tomato',
        'l': 'lettuce',
        'c': 'cheese',
        'g': 'guacamole',
        's': 'salsa'
    }
    return ['shell'] + [mapping[char] for char in word.lower() if char in mapping] + ['shell']
