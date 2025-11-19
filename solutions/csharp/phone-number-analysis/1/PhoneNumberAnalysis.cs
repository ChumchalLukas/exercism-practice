public static class PhoneNumber
{
    public static (bool IsNewYork, bool IsFake, string LocalNumber) Analyze(string phoneNumber)
    {
        bool IsNewYork = false;
        bool IsFake = false;

        string[] splitedPhoneNumber = phoneNumber.Split('-');

        if (splitedPhoneNumber[0] == "212"){
            IsNewYork = true;
        }

        if (splitedPhoneNumber[1] == "555"){
            IsFake = true;
        }

        string LocalNumber = splitedPhoneNumber[2];

        return (IsNewYork, IsFake, LocalNumber);
        
    }

    public static bool IsFake((bool IsNewYork, bool IsFake, string LocalNumber) phoneNumberInfo)
    {
        return phoneNumberInfo.IsFake;
        
    }
}
