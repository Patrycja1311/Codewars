def michael_pays(cost):
    return round(cost if cost < 5 else cost - min(cost / 3, 10), 2)
