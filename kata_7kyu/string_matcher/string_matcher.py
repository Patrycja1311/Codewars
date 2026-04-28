def is_matching(st, st1, st2):
    from collections import Counter

    def clean(text):
        return ''.join(c.lower() for c in text if c.isalpha())

    return Counter(clean(st)) == Counter(clean(st1) + clean(st2))
