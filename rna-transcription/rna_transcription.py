def to_rna(dna_strand):
    rna = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }

    if dna_strand == "":
        return ""
    else:
        result = ""
        for c in dna_strand:
            result += rna[c]
        return result
