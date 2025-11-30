public static class SquareRoot
{
    public static int Root(int number)
    {
        double squareRootNumber = Math.Pow(number, 0.5);

        return (int)Math.Round(squareRootNumber);
    }
}
