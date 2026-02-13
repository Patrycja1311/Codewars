def sort_cards(cards):
    order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    rank_index = {card: i for i, card in enumerate(order)}
    return sorted(cards, key=lambda x: rank_index[x])