def to_rna(dna_strand):
    dna_to_rna_map = {
            'G':'C',
            'C':'G',
            'T':'A',
            'A':'U'
            }
    
    rna_strand = ''
    for nucl in dna_strand:
        try:
            rna_strand += dna_to_rna_map[nucl]
        except KeyError:
           return '' 
    return rna_strand


