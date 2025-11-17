public static class LogAnalysis 
{
    // TODO: define the 'SubstringAfter()' extension method on the `string` type

    public static string SubstringAfter(this string logLine, string stringSeparator){

        int indexOfSeparator = logLine.IndexOf(stringSeparator);
        int lenghtOfSubstring = stringSeparator.Length;

        return logLine.Substring(indexOfSeparator + stringSeparator.Length);

    }

    // TODO: define the 'SubstringBetween()' extension method on the `string` type

    public static string SubstringBetween(this string logLine, string separatorBefore, string separatorAfter){
        int indexSeparatorBefore = logLine.IndexOf(separatorBefore) + separatorBefore.Length;
        int indexSeparatorAfter = logLine.IndexOf(separatorAfter);

        return logLine[indexSeparatorBefore .. indexSeparatorAfter];
        
        
    }
    
    // TODO: define the 'Message()' extension method on the `string` type

    public static string Message(this string logLine ){

        return logLine.SubstringAfter(": ");

        
        
    }

    // TODO: define the 'LogLevel()' extension method on the `string` type

    public static string LogLevel(this string logLine){

        return logLine.SubstringBetween("[","]");
        
    }
}