def proteins(strand):
    codon = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP"
    }

    result = []
    x = 0

    while True:
        if x*3+1 <= len(strand) and strand[x*3:x*3+3] not in ["UAA", "UAG", "UGA", ""]:
            result.append(codon[strand[x*3:x*3+3]])
            x += 1
        else:
            break
    
    return result
