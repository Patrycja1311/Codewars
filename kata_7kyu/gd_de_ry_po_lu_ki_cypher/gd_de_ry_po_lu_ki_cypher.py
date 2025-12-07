def encode(message):
    key = "GADERYPOLUKI"
    trans = {}
    for a, b in zip(key[::2], key[1::2]):
        trans[a], trans[b] = b, a
        trans[a.lower()], trans[b.lower()] = b.lower(), a.lower()
    return "".join(trans.get(c, c) for c in message)


def decode(message):
    return encode(message)
