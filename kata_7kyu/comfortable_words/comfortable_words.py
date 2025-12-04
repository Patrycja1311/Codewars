def comfortable_word(word):
    left = set("qwertasdfgzxcvb")
    right = set("yuiophjklnm")
    return all((word[i] in left) != (word[i+1] in left) for i in range(len(word)-1))
