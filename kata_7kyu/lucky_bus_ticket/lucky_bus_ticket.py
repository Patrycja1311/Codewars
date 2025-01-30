def is_lucky(ticket):
    return ticket.isdigit() and len(ticket) == 6 and sum(map(int, ticket[:3])) == sum(map(int, ticket[3:]))
