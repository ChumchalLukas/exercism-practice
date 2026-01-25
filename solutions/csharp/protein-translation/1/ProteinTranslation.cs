public static class ProteinTranslation
{

      // Codon database:
          private static readonly Dictionary<string, string> codonsToAmino = new()
    {
        ["AUG"] = "Methionine",
        ["UUU"] = "Phenylalanine",
        ["UUC"] = "Phenylalanine",
        ["UUA"] = "Leucine",
        ["UUG"] = "Leucine",
        ["UCU"] = "Serine",
        ["UCC"] = "Serine",
        ["UCA"] = "Serine",
        ["UCG"] = "Serine",
        ["UAU"] = "Tyrosine",
        ["UAC"] = "Tyrosine",
        ["UGU"] = "Cysteine",
        ["UGC"] = "Cysteine",
        ["UGG"] = "Tryptophan",
        ["UAA"] = "STOP",
        ["UAG"] = "STOP",
        ["UGA"] = "STOP"
    };




    
    public static string[] Proteins(string strand)
    {
        int arraySize = strand.Length / 3;
        int indexCounter = 0;
        List<string> convertedStrand = new List<string>{};

        string codon;
        string aminoacid;
        int strandIndex = 0;

        while (indexCounter < arraySize)
        {
            // Splited codon:
            codon = strand.Substring(strandIndex, 3);

            // Converted aminoacid: 
            aminoacid = ConvertCodon(codon);

            // Stop codons check:
            if(aminoacid == "STOP")
            {
                break;
            };

            convertedStrand.Add(aminoacid);

            strandIndex += 3;
            indexCounter++;
        };

        return convertedStrand.ToArray();
    }


    private static string ConvertCodon(string codon)
    {
     // Codon to amino acid:
     if (codon.Length < 3 || codon.Length > 3)
    {
        throw new ArgumentException("Entry has to be 3 letters long.");
    };

    if (codonsToAmino.ContainsKey(codon))
    {
        return codonsToAmino[codon];
    } else 
    {
        throw new KeyNotFoundException($"{codon} not in database.");
    };
        
    }
}