using System.Text;

public static class Identifier
{
    public static string Clean(string identifier)
    {       
        StringBuilder correctedIdentifier = new StringBuilder(identifier);

        
    

        

        // replace whitespaces: 
        
        if(identifier.Contains(" "))
        {
          correctedIdentifier.Replace(' ', '_');
        }

        // replace controlcharacters: 

        ReplaceControlChars(correctedIdentifier);


        // replace kebab-case:

        if(identifier.Contains("-"))
        {
            for(int index = 0; index < identifier.Length; index++)
            {
                if(identifier[index] == '-' && index + 1 < identifier.Length)
                {
                    correctedIdentifier[index + 1] = char.ToUpper(correctedIdentifier[index+1]);
                }

            }

            correctedIdentifier.Replace("-","");
        }

        // replace non-letter characters:

        DeleteNonLetter(correctedIdentifier);


        // omit greek:

        NoGreek(correctedIdentifier);

        
        

        return correctedIdentifier.ToString();

        
    }

    // non-letter out method: 
    private static void DeleteNonLetter(StringBuilder sb)
        {
            for (int i = sb.Length - 1; i >= 0; i--)
        {
                
                if (!char.IsLetter(sb[i]) && sb[i] != '_')
                {
                    sb.Remove(i, 1); 
                }
        }
    }

    // no greek letters:

    private static void NoGreek(StringBuilder sb)
    {
    for (int i = sb.Length - 1; i >= 0; i--)
    {
        int code = sb[i];
        
        if (code >= 945 && code <= 969)
        {
            sb.Remove(i, 1);
        }
    }
    }

    private static void ReplaceControlChars(StringBuilder sb)
{
    for (int i = sb.Length - 1; i >= 0; i--)
    {
        if (char.IsControl(sb[i]))
        {
            sb.Remove(i, 1);
            sb.Insert(i, "CTRL");
        }
    }
}

}
