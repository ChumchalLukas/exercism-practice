public static class ResistorColorDuo
{
    public static int Value(string[] colors)
    {
        string resistorValue = "";

        foreach(string color in colors)
        {
            string colorValue = ColorResistor(color);
            resistorValue += colorValue;
        };

        string finalResistorValue = resistorValue[..2];

        return int.Parse(finalResistorValue);

        
    }

    private static string ColorResistor(string color) => color switch 
    {
            "black" => "0",
            "brown" => "1",
            "red" => "2",
            "orange" => "3",
            "yellow" => "4",
            "green" => "5",
            "blue" => "6",
            "violet" => "7",
            "grey" => "8",
            "white" => "9",
            
    };

    
}
