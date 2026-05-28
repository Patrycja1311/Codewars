def majority(arr):
    if not arr:
        return None
    counts = {x: arr.count(x) for x in set(arr)}
    best = max(counts, key=counts.get)
    if list(counts.values()).count(counts[best]) > 1:
        return None
    return best
