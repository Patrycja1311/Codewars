def get_sum(a,b):
    if a < b:
        new_list = [num for num in range(a, b+1)]
    else:
        new_list = [num for num in range(b, a+1)]
    return sum(new_list)
