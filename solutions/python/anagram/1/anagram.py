def find_anagrams(word, candidates):

    word_lower = word.lower()
    word_letter_count = {letter: word_lower.count(letter) for letter in word_lower}

    final_result = []

    for candidate in candidates:
        candidate_lower = candidate.lower()
        if candidate_lower == word_lower:
            continue  
        if len(candidate_lower) != len(word_lower):
            continue 
        candidate_letter_count = {letter: candidate_lower.count(letter) for letter in candidate_lower}
        if candidate_letter_count == word_letter_count:
            final_result.append(candidate)

    return final_result
