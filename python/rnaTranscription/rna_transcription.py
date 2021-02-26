def to_rna(dna_strand):
    rna_strand = ""
    rna_map = getDnaToRna()
    for element in dna_strand:
        if rna_map.get(element) is None:
            raise Exception("Invalid DNA Strand")
        transformed_element = rna_map.get(element)
        rna_strand += transformed_element
    return rna_strand


def getDnaToRna():
    rna_map = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    return rna_map
