def bucket_of(said):
    said = said.lower()

    water = any(x in said for x in ["water", "wet", "wash"])
    slime = any(x in said for x in ["i don't know", "slime"])

    if water and slime:
        return "sludge"
    elif water:
        return "water"
    elif slime:
        return "slime"
    else:
        return "air"
