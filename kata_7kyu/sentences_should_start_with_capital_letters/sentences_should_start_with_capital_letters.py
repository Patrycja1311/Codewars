def fix(paragraph):
    parts = paragraph.split('. ')
    return '. '.join(p.capitalize() for p in parts)
