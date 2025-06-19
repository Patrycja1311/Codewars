def valid_card(card):
    digits = [int(d) for d in card.replace(" ", "")][::-1]
    digits = [d if i % 2 == 0 else (d * 2 - 9 if d * 2 > 9 else d * 2) for i, d in enumerate(digits)]
    return sum(digits) % 10 == 0
