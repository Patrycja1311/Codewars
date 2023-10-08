def alphabet_war(fight):
    power = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1}
    total_score = sum(power.get(letter, 0) for letter in fight)

    if total_score > 0:
        return "Left side wins!"
    elif total_score < 0:
        return "Right side wins!"
    else:
        return "Let's fight again!"
