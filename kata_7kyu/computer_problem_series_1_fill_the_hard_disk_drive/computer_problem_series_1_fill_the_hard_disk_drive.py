def save(sizes, hd):
    total_size = count = 0
    for size in sizes:
        if total_size + size > hd and size != 0:
            break
        total_size += size
        count += 1
    return count
