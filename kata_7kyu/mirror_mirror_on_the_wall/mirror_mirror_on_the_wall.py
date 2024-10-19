def mirror(data: list) -> list:
    if not data:
        return []
    sorted_arr = sorted(data)
    return sorted_arr + sorted_arr[-2::-1]
