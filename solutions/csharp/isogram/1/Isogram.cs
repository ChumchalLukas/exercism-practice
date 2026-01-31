using System;
using System.Collections.Generic;

public static class Isogram
{
    public static bool IsIsogram(string word)
    {

        // Creating input without non-letters symbols:

        string lowerWord = word.ToLower();
        List<char> wordLetters = new List<char>();

        foreach(char symbol in lowerWord)
        {

            if(Char.IsLetter(symbol))
            {
                wordLetters.Add(symbol);
            };
            
        }

        // Creating wordLetters - no duplicates 

        HashSet<char> uniqueWordLetters = new HashSet<char>(wordLetters);

        return wordLetters.Count == uniqueWordLetters.Count;
        
    }
}
