def to24hourtime(hour, minute, period):
    hour = hour % 12
    if period == 'pm':
        hour += 12
    return f'{hour:02d}{minute:02d}'
