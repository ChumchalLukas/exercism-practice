public static class ResistorColorDuo
{
    // Resistor lookup table:
    private static readonly Dictionary<string, string> colorResistorTable = new Dictionary<string,string>
    {
        {"black", "0"},
        {"brown", "1"},
        {"red", "2"},
        {"orange", "3"},
        {"yellow", "4"},
        {"green", "5"},
        {"blue", "6"},
        {"violet", "7"},
        {"grey", "8"},
        {"white", "9"}
    };

    
    
    public static int Value(string[] colors)
    {
        string resistorValue = "";

        for(int index = 0; index < 2; index++)
        {

            string colorValue = ColorResistor(colors[index]);
            resistorValue += colorValue;
            
        }

        return int.Parse(resistorValue);

        
    }

    private static string ColorResistor(string color) => colorResistorTable.ContainsKey(color)?colorResistorTable[color]:throw new KeyNotFoundException("Key is not in reference table");

    
}
