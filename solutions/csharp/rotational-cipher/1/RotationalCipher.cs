using System;
using System.Text;

public static class RotationalCipher
{
    private static string abcLower = "abcdefghijklmnopqrstuvwxyz";
    private static string abcUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
    public static string Rotate(string text, int shiftKey)
    {
        char[] charedText = text.ToCharArray();
        var sb = new StringBuilder();

        foreach(char symbol in charedText)
        {
            if(Char.IsLetter(symbol))
            {
                if(abcLower.Contains(symbol))
                {
                    int symbolAbcLower = abcLower.IndexOf(symbol);
                    int symbolAbcLowerCiphered = symbolAbcLower + shiftKey;

                    char cipheredLowerLetter = abcLower[symbolAbcLowerCiphered % abcLower.Length];
                    sb.Append(cipheredLowerLetter);
                    
                } else
                {
                    int symbolAbcUpper = abcUpper.IndexOf(symbol);
                    int symbolAbcUpperCiphered = symbolAbcUpper + shiftKey;

                    char cipheredUpperLetter = abcUpper[symbolAbcUpperCiphered % abcUpper.Length];
                    sb.Append(cipheredUpperLetter);
                    
                }
                
            } else {
                sb.Append(symbol);
            }
        }

        return sb.ToString();
        
    }

    
}