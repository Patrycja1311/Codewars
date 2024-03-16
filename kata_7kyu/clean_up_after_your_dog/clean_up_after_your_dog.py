def crap(garden, bags, cap):
    crap_count = sum(row.count('@') for row in garden)
    if any('D' in row for row in garden):
        return 'Dog!!'
    return 'Clean' if bags * cap >= crap_count else 'Cr@p'
