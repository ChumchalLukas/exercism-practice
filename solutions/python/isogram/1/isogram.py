def is_isogram(word):
    """ __summary__

    Check if a word is an isogram.

    An isogram is a word with no repeating letters (case-insensitive).
    Spaces and hyphens are ignored.

    Args:
        word (str): The word to check.

    Returns:
        bool: True if the word is an isogram, False otherwise.
    
    """

    
    word_updated = []
    
    # modify input
    for i in word:
        if i == " " or i == "-":
            continue
        word_updated.append(i.lower())

    return len(word_updated) == len(set(word_updated))
