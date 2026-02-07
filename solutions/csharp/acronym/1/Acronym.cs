using System.Collections.Generic;

public static class Acronym
{
    public static string Abbreviate(string phrase)
    {
        
        List<string> abbreviation = new List<string>();

        char[] delimeters = new char[] {' ', '-','_'};
    
        string[] splittedPhrase = phrase.ToUpper().Split(delimeters, StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);

        foreach(string word in splittedPhrase)
        {

            abbreviation.Add(word[0].ToString());
            
        }

        return string.Concat(abbreviation);
    }
}