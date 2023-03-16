def xo(s):
    list_o = [elem for elem in s.lower() if elem == 'o']
    list_x = [elem for elem in s.lower() if elem == 'x']
    return len(list_o) == len(list_x)