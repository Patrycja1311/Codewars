def cat_mouse(x):
    cat_index = x.find('C')
    mouse_index = x.find('m')
    distance = abs(cat_index - mouse_index) - 1
    if distance <= 3:
        return 'Caught!'
    else:
        return 'Escaped!'
