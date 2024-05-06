def how_many_times(annual_price, individual_price):
    return -(-annual_price // individual_price) if annual_price > 0 and individual_price > 0 else "Prices must be positive."
