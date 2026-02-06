def game(words):
    if not words or words[0] == "":
        return []

    result = [words[0]]

    for w in words[1:]:
        if w == "" or w[0] != result[-1][-1]:
            break
        result.append(w)

    return result
