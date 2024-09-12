def get_strings(city):
    city = city.lower()
    return ",".join(f"{char}:{'*' * city.count(char)}" for char in dict.fromkeys(city) if char.isalpha())
