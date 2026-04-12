def content_weight(bottle_weight, scale):
    x = int(scale.split()[0])
    if "larger" in scale:
        return bottle_weight * x // (x + 1)
    else:
        return bottle_weight // (x + 1)