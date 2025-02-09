def format_poem(poem):
    sentences = poem.split('. ')
    formatted_poem = '.\n'.join(sentences)
    return formatted_poem
