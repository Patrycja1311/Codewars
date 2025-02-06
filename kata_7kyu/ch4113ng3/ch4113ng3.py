def nerdify(txt):
    replacements = {'a': '4', 'A': '4', 'e': '3', 'E': '3', 'l': '1'}
    return ''.join(replacements.get(char, char) for char in txt)
