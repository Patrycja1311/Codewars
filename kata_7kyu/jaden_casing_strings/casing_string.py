def to_jaden_case(string):
    string_list = string.split(' ')
    new_string = []
    for word in string_list:
        new_string.append(word.capitalize())
    return ' '.join(new_string)