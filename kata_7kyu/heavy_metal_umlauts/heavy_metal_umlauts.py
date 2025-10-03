def heavy_metal_umlauts(boring_text):
    return boring_text.translate(str.maketrans({
        "A": "Ä", "E": "Ë", "I": "Ï", "O": "Ö", "U": "Ü", "Y": "Ÿ", "a": "ä", "e": "ë", "i": "ï", "o": "ö", "u": "ü", "y": "ÿ"
    }))
