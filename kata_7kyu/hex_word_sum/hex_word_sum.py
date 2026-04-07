def hex_word_sum(s):
    return sum(
        int(w.replace('O', '0').replace('S', '5'), 16)
        for w in s.split()
        if all(c in "0123456789ABCDEF" for c in w.replace('O', '0').replace('S', '5'))
    )
