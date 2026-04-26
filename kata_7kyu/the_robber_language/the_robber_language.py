def robber_encode(sentence):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    result = []
    for ch in sentence:
        if ch in consonants:
            if ch.isupper():
                result.append(ch + "O" + ch)
            else:
                result.append(ch + "o" + ch)
        else:
            result.append(ch)
    return "".join(result)
