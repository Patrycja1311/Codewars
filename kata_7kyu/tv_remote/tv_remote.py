def tv_remote(word):
    keyboard = ["abcde123", "fghij456", "klmno789", "pqrst.@0", "uvwxyz_/"]
    char_pos = {char: (r, c) for r, row in enumerate(keyboard) for c, char in enumerate(row)}
    x, y, total_presses = 0, 0, 0

    for char in word:
        target_x, target_y = char_pos[char]
        total_presses += abs(target_x - x) + abs(target_y - y) + 1
        x, y = target_x, target_y

    return total_presses
