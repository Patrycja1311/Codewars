def t_area(t_str):
    lines = t_str.strip().split('\n')
    height = sum(1 for line in lines if ' ' in line)
    return (height ** 2) / 2
