def der_die_das(wort):
    v = sum(c in 'aeiouäöüAEIOUÄÖÜ' for c in wort)
    return ('das ', 'die ', 'der ')[(v > 1) + (v > 3)] + wort
