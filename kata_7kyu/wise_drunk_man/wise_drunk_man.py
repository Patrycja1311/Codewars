def wdm(talk):
    return " ".join(w for w in talk.split() if w not in ("puke","hiccup"))
