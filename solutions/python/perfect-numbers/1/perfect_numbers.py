def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    Arguments:  number - positive integer
    Returns: str - integers selected category

    """

    # Errors - input data type; value
    
    if not isinstance(number, int):
        raise ValueError('Use only integers.')
    
    if number <= 0:
        raise ValueError('Classification is only possible for positive integers.')

    # Function - generation factors, summing
    
    number_factors_sum = sum(i for i in range(1, number) if (number % i) == 0)
   

    # Classifying number's category
    
    # Edge case
    if number == 1:
        return "deficient"
    
    if number == number_factors_sum:
        return "perfect"
    elif number > number_factors_sum:
        return "deficient"
    else:
        return "abundant"

    
