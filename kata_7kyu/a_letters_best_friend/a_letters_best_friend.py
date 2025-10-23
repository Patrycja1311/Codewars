def best_friend(txt, a, b):
    return all(i < len(txt)-1 and txt[i+1] == b for i in range(len(txt)) if txt[i] == a)
