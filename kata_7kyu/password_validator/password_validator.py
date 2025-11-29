def password(st):
    return (
        len(st) >= 8 and
        any(c.isupper() for c in st) and
        any(c.islower() for c in st) and
        any(c.isdigit() for c in st)
    )
