class Quark(object):
    def __init__(self, color, flavor):
        valid_colors = {"red", "blue", "green"}
        valid_flavors = {"up", "down", "strange", "charm", "top", "bottom"}

        if color not in valid_colors:
            raise ValueError(f"Invalid color: {color}. Must be one of {valid_colors}")
        if flavor not in valid_flavors:
            raise ValueError(f"Invalid flavor: {flavor}. Must be one of {valid_flavors}")

        self.color = color
        self.flavor = flavor
        self.baryon_number = 1 / 3

    def interact(self, other):
        if not isinstance(other, Quark):
            raise TypeError("Interaction must be with another Quark")
        self.color, other.color = other.color, self.color
