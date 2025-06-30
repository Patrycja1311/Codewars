def get_section_id(scroll, sizes):
    start = 0
    for i, height in enumerate(sizes):
        if start <= scroll < start + height:
            return i
        start += height
    return -1
