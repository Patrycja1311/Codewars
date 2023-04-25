def spin_words(sentence):
    split_sentence = sentence.split()
    new_sentence = [word[::-1] if len(word) >= 5 else word for word in split_sentence]
    return ' '. join(new_sentence)