def sort_my_string(s):
    even_group = s[::2]
    odd_group = s[1::2]
    return even_group + ' ' + odd_group
