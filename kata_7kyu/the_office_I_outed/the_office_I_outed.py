def outed(meet, boss):
    return 'Get Out Now!' if sum(meet[p] * (2 if p == boss else 1) for p in meet) / len(meet) <= 5 else 'Nice Work Champ!'
