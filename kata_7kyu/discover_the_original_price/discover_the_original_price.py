def discover_original_price(discounted_price, sale_percentage):
    original_price = discounted_price / (1 - (sale_percentage / 100))
    return round(original_price, 2)
