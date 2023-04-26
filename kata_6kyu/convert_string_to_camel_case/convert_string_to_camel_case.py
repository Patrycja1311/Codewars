def to_camel_case(text):
    if text == '':
        return ''
    else:
        new_text = text.replace('-', ' ').replace('_', ' ')
        words = new_text.split()
        new_words = [word.title() for word in words[1:]]
        return words[0] + ''.join(new_words)
