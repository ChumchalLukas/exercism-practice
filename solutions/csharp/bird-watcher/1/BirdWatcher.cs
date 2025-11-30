class BirdCount
{
    private int[] birdsPerDay;

    public BirdCount(int[] birdsPerDay)
    {
        this.birdsPerDay = birdsPerDay;
    }

    public static int[] LastWeek()
    {
        return new int[] { 0, 2, 5, 3, 7, 8, 4 };
    }

    public int Today()
    {
        return birdsPerDay[birdsPerDay.Length - 1];
    }

    public void IncrementTodaysCount()
    {
        birdsPerDay[birdsPerDay.Length - 1] += 1;
    }

    public bool HasDayWithoutBirds()
    {
        foreach(int item in birdsPerDay)
        {
            if(item == 0){
                return true;
            }
        }

        return false;
    }

    public int CountForFirstDays(int numberOfDays)
    {
        int birdsPerSpecifiedDays = 0;

        for(int day = 0 ; day < numberOfDays; day++)
        {
            birdsPerSpecifiedDays += birdsPerDay[day];
        } 

        return birdsPerSpecifiedDays;
    }

    public int BusyDays()
    {
        int busyDays = 0;

        for(int day = 0; day < birdsPerDay.Length; day++)
        {
            if(birdsPerDay[day] >= 5){
                busyDays++;
            }
        }

        return busyDays;
    }
}
