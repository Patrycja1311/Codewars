def split_the_bill(x):
    avg = sum(x.values()) / len(x)
    return {k: round(v - avg, 2) for k, v in x.items()}
