def nothing_special(st):
    if not isinstance(st, str):
        return "Not a string!"
    return ''.join(c for c in st if c.isalnum() or c.isspace())
