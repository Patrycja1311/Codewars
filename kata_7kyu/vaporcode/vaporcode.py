def vaporcode(s):
    return "  ".join(s.upper()).replace(" ", "").replace("", "  ")[2:-2]
