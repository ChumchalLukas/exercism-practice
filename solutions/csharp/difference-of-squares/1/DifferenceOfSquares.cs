public static class DifferenceOfSquares
{
    public static int CalculateSquareOfSum(int max) => (int)Math.Pow(Enumerable.Range(1, max).Sum(), 2);
    
    public static int CalculateSumOfSquares(int max)
    {
        int[] numberToMax = new int[max];

        for(int num = 1; num <= max; num++){

            numberToMax[num - 1] = (int)Math.Pow(num,2);
            
        }

        return numberToMax.Sum();
    }

    public static int CalculateDifferenceOfSquares(int max)
    {
        int squareOfSum = CalculateSquareOfSum(max);
        int sumOfSquares = CalculateSumOfSquares(max);

        return squareOfSum - sumOfSquares;
    }
}