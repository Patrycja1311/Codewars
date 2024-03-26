def remove_rotten(bag_of_fruits):
    if not bag_of_fruits:
        return []
    return [fruit[6:].lower() if fruit.startswith("rotten") else fruit.lower() for fruit in bag_of_fruits if fruit]
