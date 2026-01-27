public static class ResistorColorDuo
{
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
