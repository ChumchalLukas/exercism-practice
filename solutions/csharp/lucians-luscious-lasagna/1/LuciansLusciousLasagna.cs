class Lasagna
{
    // TODO: define the 'ExpectedMinutesInOven()' method
    
    public int ExpectedMinutesInOven(){

        int expectedTime = 40;
        
        return expectedTime;
            
    }

    // TODO: define the 'RemainingMinutesInOven()' method

    public int RemainingMinutesInOven(int bakeTime){

        int expectedTime = 40;
        
        return expectedTime - bakeTime;
    }

    // TODO: define the 'PreparationTimeInMinutes()' method

    public int PreparationTimeInMinutes(int layersNum){

        return layersNum * 2;
        
    }

    // TODO: define the 'ElapsedTimeInMinutes()' method

    public int ElapsedTimeInMinutes(int layersCount, int bakingTime){

        return (layersCount * 2) + bakingTime;
        
    }
}
