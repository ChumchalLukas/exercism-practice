public static class Bob
{
    public static string Response(string statement)
    {
        // Conditions: 
        bool endWithQuestionMark = statement.Trim().EndsWith("?");
        bool allCapitalLetters = (statement.Any(char.IsLetter)) && (statement == statement.ToUpper());
        bool allCapitalQuestion = allCapitalLetters && endWithQuestionMark;
        bool silentOrWhitespace = string.IsNullOrWhiteSpace(statement);

        if (allCapitalQuestion)
        {
            return "Calm down, I know what I'm doing!";
        } else if (endWithQuestionMark)
        {
            return "Sure.";
        } else if (allCapitalLetters)
        {
            return "Whoa, chill out!";
        } else if (silentOrWhitespace)
        {
            return "Fine. Be that way!";
        } else 
        {
            return "Whatever.";
        }
       
        
    }
}