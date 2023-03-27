def DNA_strand(dna):
    new_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(new_dict[elem] for elem in dna)
