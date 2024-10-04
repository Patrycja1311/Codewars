def compare(s1, s2):
    def clean(s):
        return sum(ord(c) for c in (s or "").upper()) if (s or "").isalpha() else 0

    return clean(s1) == clean(s2)
