"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    # convert to list
    word_list = word.split()

    # add prefix
    word_list.insert(0, "un")

    return "".join(word_list)

def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    # list for final output
    prefixed_words = []

    # add prefix

    prefix = vocab_words[0]
    prefixed_words.append(prefix)

    for word in vocab_words[1:]:

        # adding prefix to vocabulary
        modified_word =  prefix + word
        prefixed_words.append(modified_word)
        
    return " :: ".join(prefixed_words)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    # remove ness
    lst_word = list(word.removesuffix("ness"))

    # i -> y
    if lst_word[-1] == "i":
        lst_word[-1] = "y"

    return "".join(lst_word)


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    # split to list -> use index for search
    lst_sentence = sentence.split(" ")

    return lst_sentence[index].strip(".") + "en"