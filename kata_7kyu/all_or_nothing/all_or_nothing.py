def possibly_perfect(key, answers):
    return (
        all(k == "_" or k == a for k, a in zip(key, answers)) or
        all(k == "_" or k != a for k, a in zip(key, answers))
    )
