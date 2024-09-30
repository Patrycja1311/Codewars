def get_issuer(number):
    num_str = str(number)

    if len(num_str) == 15 and num_str[:2] in ["34", "37"]:
        return "AMEX"
    if len(num_str) == 16 and num_str.startswith("6011"):
        return "Discover"
    if len(num_str) == 16 and num_str[:2] in ["51", "52", "53", "54", "55"]:
        return "Mastercard"
    if len(num_str) in [13, 16] and num_str.startswith("4"):
        return "VISA"

    return "Unknown"
