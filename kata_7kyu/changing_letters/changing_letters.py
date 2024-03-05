def swap(st):
    vowels = "aeiouAEIOU"
    return ''.join(char.upper() if char in vowels else char for char in st)
