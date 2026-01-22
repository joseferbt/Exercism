import re

def to_rna(dna_strand):
    rna = ''
    for i in dna_strand:
        if i == 'C':
            rna += 'G'
        elif i == 'G':
            rna += 'C'
        elif i == 'T':
            rna += 'A'
        elif i == 'A':
            rna += 'U'
    return rna