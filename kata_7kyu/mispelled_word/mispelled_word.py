def mispelled(word1, word2):
    if word1 == word2:
        return True
    if abs(len(word1) - len(word2)) == 1:
        return word1 in (word2[1:], word2[:-1]) or word2 in (word1[1:], word1[:-1])
    if len(word1) == len(word2):
        return sum(a != b for a, b in zip(word1, word2)) <= 1
    return False
