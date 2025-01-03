def sort_bytes(number):
    if not (0 <= number <= 0xFFFFFFFF):
        raise ValueError("Input must be an unsigned 32-bit integer.")
    bytes_list = sorted([(number >> (8 * i)) & 0xFF for i in range(4)], reverse=True)
    return sum(byte << (8 * (3 - i)) for i, byte in enumerate(bytes_list))
