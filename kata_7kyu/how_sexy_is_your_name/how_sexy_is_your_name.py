def sexy_name(name):
    s = sum(SCORES.get(c.upper(), 0) for c in name)
    return ('NOT TOO SEXY', 'PRETTY SEXY', 'VERY SEXY', 'THE ULTIMATE SEXIEST')[
        (s > 60) + (s > 300) + (s > 599)
    ]
