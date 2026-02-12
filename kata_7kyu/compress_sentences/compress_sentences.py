def compress(sentence):
    words = sentence.split()
    seen = {}
    result = []
    index = 0
    for word in words:
        w = word.lower()
        if w not in seen:
            seen[w] = index
            index += 1
        result.append(str(seen[w]))
    return "".join(result)
