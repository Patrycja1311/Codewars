def sort_grades(lst):
    return sorted(lst, key=lambda x: -1 if x=='VB' else 0 if x=='V0' else 0.5 if x=='V0+' else int(x[1:]))
