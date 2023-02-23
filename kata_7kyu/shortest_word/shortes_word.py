def find_short(s):
    new_list = []
    [new_list.append(len(i)) for i in s.split(" ")]
    return sorted(new_list)[0]