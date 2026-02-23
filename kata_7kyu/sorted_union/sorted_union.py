def unite_unique(*arrays):
    seen = set()
    result = []
    for arr in arrays:
        for value in arr:
            if value not in seen:
                seen.add(value)
                result.append(value)
    return result
