def steps(number):
    """Counting steps of collatz sequence:
    
    input:    
    parm: number -> int

    output:
    repeat: number -> int # steps of sequence
    
    """

    # Exceptions:

    # if not isinstance(number, int):
    #     raise TypeError("Input have to be integer!")

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    # Main:

    steps_count = 0

    if number == 1:
        return steps_count

    while True:
        
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
            

        steps_count += 1

        if number == 1:
            break


    return steps_count




        
