public class Anagram
{
    private string baseWord;
    
    public Anagram(string baseWord)
    {
        this.baseWord = baseWord;
    }

    public string[] FindAnagrams(string[] potentialMatches)
    {
        // elements - not equal char counts;

        // elements - not equal char contant;

        // elements - baseWord not equal to word;

        List<string> possibleAnagrams = new List<string>();

        foreach(string word in potentialMatches)
        {
             bool checkAnagram = (word.Length == baseWord.Length) && 
            (word.ToLower() != baseWord.ToLower()) &&                                              (String.Concat(word.ToLower().OrderBy(c => c)) ==
             String.Concat(baseWord.ToLower().OrderBy(c => c)));

            if(checkAnagram)
            {
                possibleAnagrams.Add(word);
            } else
            {
                continue;
            }
            
            
        }
        

        return possibleAnagrams.ToArray();



    }
}