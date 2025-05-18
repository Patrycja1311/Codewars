def bald(s):
    c = s.count("/")
    return [s.replace("/", "-"), ["Clean!", "Unicorn!", "Homer!", "Careless!", "Careless!", "Careless!", "Hobo!"][min(c, 6)]]
