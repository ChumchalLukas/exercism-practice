static class SavingsAccount
{
    public static float InterestRate(decimal balance)
    {
        switch (balance){
            case < 0:
                return 3.213f;
                break;
            
            case >= 0 and < 1000:
                return 0.5f;
                break;

            case >= 1000 and < 5000:
                return 1.621f;
                break;

            case >= 5000:
                return 2.475f;
                break;
                
        }
        
    }

    public static decimal Interest(decimal balance)
    {
       float basicInterestRate = SavingsAccount.InterestRate(balance);
        decimal interestFinal = (balance * (decimal)basicInterestRate)/100;


        return interestFinal;
    }

    public static decimal AnnualBalanceUpdate(decimal balance) => balance + ((decimal)SavingsAccount.InterestRate(balance)/100 * balance);

      public static int YearsBeforeDesiredBalance(decimal balance, decimal targetBalance)
    {
        int years = 0;

        
        while (balance < targetBalance)
        {
            balance = AnnualBalanceUpdate(balance);
            years++;
        }

        return years;
    }

}
