public static class ReverseString
{
    public static string Reverse(string input)
    {
        char[] wordInput = input.ToCharArray();
        char[] wordReversed = new char[input.Length];

        int readIndex = input.Length - 1;

        for(int writeIndex = 0; writeIndex < input.Length; writeIndex++)
        {
            wordReversed[writeIndex] = wordInput[readIndex];

            readIndex--;
            
        }

        return new string(wordReversed);
    }
}