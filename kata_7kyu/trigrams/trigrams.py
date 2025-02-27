def trigrams(phrase):
    return " ".join(phrase.replace(" ", "_")[i:i+3] for i in range(len(phrase) - 2)) if len(phrase) > 2 else ""
