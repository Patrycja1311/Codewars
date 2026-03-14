def queue(queuers, pos):
    t = queuers[pos]
    return sum(min(x, t) if i <= pos else min(x, t-1) for i, x in enumerate(queuers))
