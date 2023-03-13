import math

def buses(kids, adults, places):
    if places < 3:
        return 0
    elif adults < math.ceil(kids/(places-2)) * 2:
        return 0
    else:
        return math.ceil((kids+adults)/places)