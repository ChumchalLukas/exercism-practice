def is_armstrong_number(number):
    """Check for armstrong number"""

    # digits count, each digit separately, arnold number placeholder
    
    digits_count = len(list(str(number)))
    numbers = tuple(str(number))
    arnotld_check = 0 

    for num in numbers:

        arnotld_check += int(num) ** int(digits_count)

    return True if arnotld_check == number else False