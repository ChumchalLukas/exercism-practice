static class AssemblyLine
{
    public static double SuccessRate(int speed)
    {
        if (speed == 0){
            return 0.0;
        } else if(speed >= 1 && speed <= 4){
            return 1.0;
        } else if(speed >= 5 && speed <= 8){
            return 0.9;
        } else if(speed == 9){
            return 0.8;
        } else if(speed == 10){
            return 0.77;
        } 

        return -1;
    }
    
    public static double ProductionRatePerHour(int speed)
    {
        const int carsPerHour = 221;
        double productionSuccess = AssemblyLine.SuccessRate(speed);

        double productionFinal = (carsPerHour * speed) * productionSuccess;

        return productionFinal;
        
    }

    public static int WorkingItemsPerMinute(int speed)
    {
        return (int)AssemblyLine.ProductionRatePerHour(speed)/60;
    }
}
