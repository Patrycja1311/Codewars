import math


def movie(card, ticket, perc):
    n = 0
    total_cost_B = card
    current_ticket_price = ticket * perc
    while math.ceil(total_cost_B + current_ticket_price * (1 - perc ** n) / (1 - perc)) >= ticket * n:
        n += 1
    return n
