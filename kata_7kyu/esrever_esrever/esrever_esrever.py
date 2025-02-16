def esrever(st):
    if not st:
        return ""
    return ' '.join(word[::-1] for word in st[:-1].split()[::-1]) + (st[-1] if st[-1] in "!?." else "")
