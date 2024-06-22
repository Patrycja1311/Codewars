def duplicates(arr):
    seen, duplicates, result = set(), set(), []
    for elem in arr:
        if elem in seen and elem not in duplicates:
            result.append(elem)
            duplicates.add(elem)
        seen.add(elem)
    return result
