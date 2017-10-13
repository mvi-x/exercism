def to_rna(dna_strand):
    # attention! order of the items in the tuples below is essential. do not change.
    valid_dna_nucl = ('G', 'C', 'T', 'A')
    valid_rna_nucl = ('C', 'G', 'A', 'U')
    
    rna_strand = ''
    for nucl in dna_strand:
        try:
            i = valid_dna_nucl.index(nucl)
            rna_strand += valid_rna_nucl[i]
        except ValueError:
           return '' 
    return rna_strand


