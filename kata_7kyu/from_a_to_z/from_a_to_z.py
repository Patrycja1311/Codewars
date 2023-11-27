def gimme_the_letters(sp):
    return ''.join([chr(i) for i in range(ord(sp[0]), ord(sp[-1])+1)])
