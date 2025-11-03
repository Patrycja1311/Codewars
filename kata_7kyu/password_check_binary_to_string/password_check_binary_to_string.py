def decode_pass(pass_list, bits):
    return next((s for s in (''.join(chr(int(b, 2)) for b in bits.split()),) if s in pass_list), False)
