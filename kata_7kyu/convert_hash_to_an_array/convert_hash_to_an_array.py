def convert_hash_to_array(dct):
    return [[key, value] for key, value in sorted(dct.items())]
