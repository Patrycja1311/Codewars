def switch_dict(dic):
    out = {}
    for k, v in dic.items():
        out.setdefault(v, []).append(k)
    return out
