public static class Darts
{
    public static int Score(double x, double y)
    {
       double distanceFromMiddpoint = Math.Sqrt(Math.Pow(x,2) + Math.Pow(y,2));

        if (distanceFromMiddpoint <= 1){
            return 10;
        } else if (distanceFromMiddpoint > 1 && distanceFromMiddpoint <= 5){
            return 5;
        } else if (distanceFromMiddpoint > 5 && distanceFromMiddpoint <= 10){
            return 1;
        } else{
            return 0;
        }
    }
}
