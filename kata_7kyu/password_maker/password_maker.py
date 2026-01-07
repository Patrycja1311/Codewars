def make_password(phrase):
    return ''.join({'i': '1', 'o': '0', 's': '5'}.get(c.lower(), c) for c in (w[0] for w in phrase.split()))
