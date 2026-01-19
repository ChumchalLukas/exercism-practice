public class SpaceAge
{
    private double basicYear;
    
    public SpaceAge(int seconds)
    {
        this.basicYear = seconds / (double) 31557600;
    }

    public double OnEarth()
    {
      return basicYear;
    }

    public double OnMercury()
    {
        return basicYear / 0.2408467;
    }

    public double OnVenus()
    {
        return basicYear / 0.61519726;
    }

    public double OnMars()
    {
        return basicYear / 1.8808158;
    }

    public double OnJupiter()
    {
       return basicYear / 11.862615;
    }

    public double OnSaturn()
    {
        return basicYear / 29.447498;
    }

    public double OnUranus()
    {
        return basicYear / 84.016846;
    }

    public double OnNeptune()
    {
       return basicYear / 164.79132;
    }
}