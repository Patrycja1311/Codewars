def trilingual_democracy(group):
    s = set(group)
    all_langs = {'D', 'F', 'I', 'K'}

    if len(s) == 1:
        return group[0]
    if len(s) == 2:
        return next(l for l in s if group.count(l) == 1)
    return (all_langs - s).pop()
