def zebulans_nightmare(function):
    parts = function.split('_')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])
