def to_rna(dna_strand):

    """
    Return RNA complement of a DNA strand.

    Arguments:
    dna_strand -- string containing DNA nucleotides (A, C, G, T)

    Returns:
    string -- RNA strand (A->U, T->A, C->G, G->C)
    """

    RNA_complement = {
        "C" : "G",
        "A" : "U",
        "U" : "A",
        "G" : "C",
        "T" : "A"
    }

    iRNA = [RNA_complement[i] for i in list(dna_strand) if i in RNA_complement]

    return "".join(iRNA)

