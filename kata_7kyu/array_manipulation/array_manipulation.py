def array_manip(array):
    return [min([x for x in array[i+1:] if x > array[i]] or [-1]) for i in range(len(array))]