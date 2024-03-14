def nickname_generator(name):
    vowels = "aeiou"
    return name[:4] if len(name) > 3 and name[2] in vowels else name[:3] if len(name) > 3 else "Error: Name too short"
