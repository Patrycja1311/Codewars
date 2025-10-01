def convert_lojban(lojban):
    d = {"pa": "1", "re": "2", "ci": "3", "vo": "4", "mu": "5", "xa": "6", "ze": "7", "bi": "8", "so": "9", "no": "0"}
    i, out = 0, ""
    while i < len(lojban):
        for k, v in d.items():
            if lojban.startswith(k, i):
                out += v; i += len(k); break
    return int(out)
