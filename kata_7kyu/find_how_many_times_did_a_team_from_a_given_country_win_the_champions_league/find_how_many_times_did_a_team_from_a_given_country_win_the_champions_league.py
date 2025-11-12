def count_wins(winners_list, country):
    return sum(1 for team in winners_list if team['country'] == country)
