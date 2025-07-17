def check_parity(parity, bin_str):
    return (bin_str.count('1') % 2) ^ (parity == 'odd')
