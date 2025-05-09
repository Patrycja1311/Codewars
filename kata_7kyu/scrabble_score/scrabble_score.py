def scrabble_score(st):
    return sum(dict_scores[char.upper()] for char in st if char.upper() in dict_scores)
