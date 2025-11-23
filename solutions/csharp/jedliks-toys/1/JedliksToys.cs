class RemoteControlCar
{
    private int fieldDistance = 0;
    private int batteryPercentage = 100;
    
    public static RemoteControlCar Buy()
    {
        return new RemoteControlCar();
    }

    public string DistanceDisplay()
    {
        

        return $"Driven {fieldDistance} meters";
    }

    public string BatteryDisplay()
    {

        if (batteryPercentage == 0){
            return "Battery empty";
        }

        return $"Battery at {batteryPercentage}%";
    }

    public void Drive()
    {      

        if (batteryPercentage == 0){
            return;
        }
        
        fieldDistance += 20;
        batteryPercentage -= 1;
    }
}
