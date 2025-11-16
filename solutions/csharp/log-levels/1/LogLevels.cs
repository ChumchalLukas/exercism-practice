static class LogLine
{
    public static string Message(string logLine)
    {

        int separatorIndex = logLine.IndexOf(':') + 1;
        string messageOnly = logLine[separatorIndex ..];

        return messageOnly.Trim();
        
    }

    public static string LogLevel(string logLine)
    {
        int separatorIndex = logLine.IndexOf(':') - 1;
        string messageTypeOnly = logLine[1 .. separatorIndex];

        return messageTypeOnly.Trim().ToLower();
    }

    public static string Reformat(string logLine)
    {
        // Reverse message to messagetype

        // Message
        int separatorIndex1 = logLine.IndexOf(':') + 1;
        string messageOnly = logLine[separatorIndex1 ..].Trim();

        // MessageType
        int separatorIndex2 = logLine.IndexOf(':') - 1;
        string messageTypeOnly = logLine[1 .. separatorIndex2].ToLower();

        string messageReversed = $"{messageOnly} ({messageTypeOnly})";

        return messageReversed.Trim();

        
        
    }
}
