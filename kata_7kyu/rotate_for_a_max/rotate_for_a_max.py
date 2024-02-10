def max_rot(n):
    n_str = str(n)
    max_number = n
    for i in range(len(n_str)):
        n_str = n_str[:i] + n_str[i+1:] + n_str[i]
        max_number = max(max_number, int(n_str))
    return max_number
