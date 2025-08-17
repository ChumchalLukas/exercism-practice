def score(x, y):

    """_summary_

    Function: count dart target values of three circles

    Central - radius 1 unit; value 10
    Middle - radius 5 unit; value 5
    Outer - radius 10 unit; value 1

    Miss - value 0
    
    """

    # Length from dart target
    diagonal = (x ** 2 + y ** 2) ** (1/2)

    # Center
    if (diagonal <= 1):
        return 10

    # Middle 
    if (diagonal > 1) and (diagonal <= 5):
        return 5
    
    # Outer
    if (diagonal > 5) and (diagonal <= 10):
        return 1
        
    # Outside
    if (diagonal > 10):
        return 0
