def gordon(a):
    return ' '.join(word.upper().replace('A', '@').translate(str.maketrans('EIOU', '****')) + '!!!!' for word in a.split())
