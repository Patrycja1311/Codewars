def window(lngth, offst, lst):
    return [lst[i:i+lngth] for i in range(0, len(lst) - lngth + 1, offst)]
