public static class ResistorColorDuo
{
    // Resistor lookup table:

    private static readonly string[] colorResistorTable = new string[]{
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"
    };
    

    
    
    public static int Value(string[] colors)
    {

        string resistorValue = "";

        for(int index = 0; index < 2; index++)
        {

            string checkedColor = colors[index];
            int checkedTableIndex = Array.IndexOf(colorResistorTable, checkedColor);

            if (checkedTableIndex != -1)
            {
                resistorValue += $"{checkedTableIndex}";
                
            } else 
            {
               Console.WriteLine($"{checkedColor} is not a part of table."); 
            }
        }

        return int.Parse(resistorValue);

        
    }

    
}
