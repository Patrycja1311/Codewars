def get_count(sentence):
    vovels = ['a', 'e', 'i', 'o', 'u']
    return len([letter for letter in sentence if letter in vovels])
