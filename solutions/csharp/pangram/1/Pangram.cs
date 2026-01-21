public static class Pangram
{
    const string abc = "abcdefghijklmnopqrstuvwxyz";
    
    public static bool IsPangram(string input)
    {
        input = input.ToLower();
        return abc.All(c => input.Contains(c));  

        
    }
}
