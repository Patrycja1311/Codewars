import string

alphabet = list(string.ascii_lowercase)


def alphabet_position(text):
    text = text.lower()
    new_list = [alphabet.index(i) + 1 for i in text if i in alphabet]
    new_list_2 = [str(j) for j in new_list]
    return str(' '.join(new_list_2))
