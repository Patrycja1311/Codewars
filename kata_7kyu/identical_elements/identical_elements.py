def duplicate_elements(m, n):
    return bool(set(m) & set(n)) if m and n else False
