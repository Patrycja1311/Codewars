def find_e(s):
    if s is None:
        return None
    if s == "":
        return ""
    c = s.lower().count("e")
    return str(c) if c else 'There is no "e".'
