def distance(strand_a, strand_b):
    
    HAMMING_DISTANCE = 0

    # Errors:

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    for letter_a, letter_b in zip(strand_a, strand_b):
        if letter_a != letter_b:
            HAMMING_DISTANCE += 1

    return HAMMING_DISTANCE
                


