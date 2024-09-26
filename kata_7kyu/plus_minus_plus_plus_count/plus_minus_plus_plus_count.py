def catch_sign_change(lst):
    return sum((x >= 0) != (lst[i] >= 0) for i, x in enumerate(lst[1:]))
