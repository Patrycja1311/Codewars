def case_sensitive(s):
    return [(l := [c for c in s if c.isalpha() and not c.islower()]) == [], l]
