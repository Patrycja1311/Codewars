def waterbombs(fire, w):
    return sum((len(s) + w - 1) // w for s in fire.split('Y') if s)
