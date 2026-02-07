static class Appointment
{
    private static readonly DateTime anniversary = new DateTime(2019, 9, 15, 0, 0, 0);
    
    public static DateTime Schedule(string appointmentDateDescription)
    {
        return DateTime.Parse(appointmentDateDescription);
    }

    public static bool HasPassed(DateTime appointmentDate)
    {
        DateTime presentTime = DateTime.Now;
        int result = appointmentDate.CompareTo(presentTime);

        return result < 1;
    }

    public static bool IsAfternoonAppointment(DateTime appointmentDate)
    {
        return (appointmentDate.Hour >= 12)  && (appointmentDate.Hour < 18);

            
    }

    public static string Description(DateTime appointmentDate)
    {
        return $"You have an appointment on {appointmentDate.ToString()}.";
        
    }

    public static DateTime AnniversaryDate()
    {
        
    int currentYear = DateTime.Now.Year;

    return new DateTime(currentYear, 9, 15);
    }
        
    
}
