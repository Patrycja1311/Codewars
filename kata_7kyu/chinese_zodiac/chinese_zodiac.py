def chinese_zodiac(year):
    animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat",
               "Monkey", "Rooster", "Dog", "Pig"]
    elements = ["Wood", "Fire", "Earth", "Metal", "Water"]
    animal = animals[(year - 1924) % 12]
    element = elements[((year - 1924) // 2) % 5]
    return f"{element} {animal}"
