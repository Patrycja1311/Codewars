def eliminate_unset_bits(number):
    return int('1'*number.count('1') or '0', 2)
