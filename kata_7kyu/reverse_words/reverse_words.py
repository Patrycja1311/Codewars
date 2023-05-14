def reverse_words(text):
    return " ".join([elem[::-1] for elem in text.split(" ")])
