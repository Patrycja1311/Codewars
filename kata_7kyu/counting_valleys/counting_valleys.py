def counting_valleys(s):
    level = valleys = 0
    for step in s:
        prev_level = level
        level += {'U': 1, 'D': -1}.get(step, 0)
        valleys += prev_level < 0 and level == 0
    return valleys
