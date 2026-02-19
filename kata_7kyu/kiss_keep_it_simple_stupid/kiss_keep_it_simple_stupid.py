def is_kiss(words):
    w = words.split()
    return "Keep It Simple Stupid" if any(len(x) > len(w) for x in w) else "Good work Joe!"
