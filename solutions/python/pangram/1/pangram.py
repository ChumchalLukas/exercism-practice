def is_pangram(sentence):
    # Create an alphabet dictionary with all letters set to 0
    alphabet = dict.fromkeys([chr(i) for i in range(ord('a'), ord('z') + 1)], 0)

    # Convert input to lowercase
    sentence_update = sentence.lower()

    # Update dictionary with found letters
    for letter in sentence_update:
        if letter in alphabet:
            alphabet[letter] += 1  # Track occurrences (optional)

    # Check if all letters are present at least once
    return all(alphabet.values())


