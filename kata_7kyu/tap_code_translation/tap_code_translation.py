def tap_code_translation(text):
    sq = ["abcde", "fghij", "lmnop", "qrstu", "vwxyz"]
    return ' '.join(
        '.'*(r+1)+' '+'.'*(c+1)
        for ch in text
        for r, row in enumerate(sq)
        for c, cc in enumerate(row)
        if cc == ch.replace('k', 'c')
    )
