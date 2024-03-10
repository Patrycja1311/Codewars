def band_name_generator(name):
    return name.capitalize() + name[1:] if name[0].lower() == name[-1].lower() else "The " + name.capitalize()
