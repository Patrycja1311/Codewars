def is_planet_mnemonic_correct(solar_system, mnemonic):
    filtered_planets = [planet for planet in solar_system if planet != "Asteroid"]

    if not filtered_planets:
        return mnemonic == ""

    mnemonic_letters = [word[0] for word in mnemonic.split()]
    planet_letters = [planet[0] for planet in filtered_planets]

    return mnemonic_letters == planet_letters
