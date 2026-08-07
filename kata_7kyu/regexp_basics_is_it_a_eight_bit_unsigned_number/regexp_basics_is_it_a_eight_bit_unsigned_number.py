def eight_bit_number(n):
    return n.isdigit() and (n == "0" or n[0] != "0") and 0 <= int(n) <= 255

