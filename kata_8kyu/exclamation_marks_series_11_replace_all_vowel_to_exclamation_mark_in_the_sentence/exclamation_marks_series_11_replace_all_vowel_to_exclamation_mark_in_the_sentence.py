def replace_exclamation(st):
    vovels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return ''.join(['!' if char in vovels else char for char in st])
