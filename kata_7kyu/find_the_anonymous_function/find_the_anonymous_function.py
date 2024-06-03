def find_function(func, arr):
    function = next(item for item in func if callable(item))
    return list(filter(function, arr))
