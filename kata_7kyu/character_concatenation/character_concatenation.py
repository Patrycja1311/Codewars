def char_concat(word):
    return ''.join([word[i] + word[len(word) - i - 1] + str(i + 1) for i in range(len(word) // 2)])
