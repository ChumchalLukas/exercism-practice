using System;
using System.Collections.Generic; 
using System.Linq; 

public static class ScrabbleScore
{
    private static readonly Dictionary<int, string[]> ScrabbleValue = new Dictionary<int, string[]>
    {
        {1, new[] {"A","E","I","O","U","L","N","R","S","T"}},
        {2, new[] {"D","G"}},
        {3, new[] {"B","C","M","P"}},
        {4, new[] {"F", "H","V","W","Y"}},
        {5, new[] {"K"}},
        {8, new[] {"J","X"}},
        {10, new[] {"Q","Z"}}
    };

    public static int Score(string input)
    {
        
        if (string.IsNullOrWhiteSpace(input)) return 0;

        char[] charedInput = input.ToUpper().ToCharArray();
        int wordValue = 0;

        foreach (char symbol in charedInput) 
        {
            string s = symbol.ToString();

            foreach (var dictItem in ScrabbleValue)
            {
                
                if (dictItem.Value.Contains(s)) 
                {
                    wordValue += dictItem.Key; 
                    
                }
            }
        }

        return wordValue;
    }
}