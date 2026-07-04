from collections import Counter


def odd_ball(arr):
    word_counts = Counter(x for x in arr if isinstance(x, str))
    odd_word = next(word for word, count in word_counts.items() if count == 1)
    odd_index = arr.index(odd_word)
    return odd_index in [x for x in arr if isinstance(x, int)]
