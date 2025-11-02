static class QuestLogic
{
    public static bool CanFastAttack(bool knightIsAwake)
    {
        return !knightIsAwake;
    }

    public static bool CanSpy(bool knightIsAwake, bool archerIsAwake, bool prisonerIsAwake)
    {
        return knightIsAwake || archerIsAwake || prisonerIsAwake;
    }

    public static bool CanSignalPrisoner(bool archerIsAwake, bool prisonerIsAwake)
    {
        return archerIsAwake == false && prisonerIsAwake == true;
    }

    public static bool CanFreePrisoner(bool knightIsAwake, bool archerIsAwake, bool prisonerIsAwake, bool petDogIsPresent)
    {
    return ((knightIsAwake == true || knightIsAwake == false) && archerIsAwake == false && (prisonerIsAwake == true || prisonerIsAwake == false) && petDogIsPresent == true) || (knightIsAwake == false && archerIsAwake == false && prisonerIsAwake == true && petDogIsPresent == false);
    }
}
