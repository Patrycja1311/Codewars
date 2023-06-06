def printer_error(s):
    error_count = 0
    total_count = len(s)
    for char in s:
        if char > 'm':
            error_count += 1

    return f"{error_count}/{total_count}"
