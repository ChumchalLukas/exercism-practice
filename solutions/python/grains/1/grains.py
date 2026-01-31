def square(number):
    """Grains on square"""

    # Exceptions: 
    if   not(1 <= number <= 64):
        raise ValueError("square must be between 1 and 64")

    
    return pow(2, number - 1)


def total():
    """Total grains of wheat per squares"""

    return 2**64 - 1
