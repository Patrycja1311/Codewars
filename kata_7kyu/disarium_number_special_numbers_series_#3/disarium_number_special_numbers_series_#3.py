def disarium_number(number):
    return "Disarium !!" if sum(int(d) ** (i + 1) for i, d in enumerate(str(number))) == number else "Not !!"
