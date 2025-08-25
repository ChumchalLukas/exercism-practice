def is_valid(isbn):
    # constants - sum ; positional number
    is_isbn = 0
    pos_num = 10
    
    # Parsing - delete unwanted characters
    isbn_text = str(isbn).replace("-", "").replace(" ", "")
    
    # Check validity - length
    if len(isbn_text) != 10:
        return False

    # Body
    for i, val in enumerate(isbn_text):
        if val == "X":
            # X is only valid at the last position
            if i != 9:
                return False
            is_isbn += 10 * pos_num
        elif val.isdigit():
            is_isbn += int(val) * pos_num
        else:
            return False
        pos_num -= 1

    return is_isbn % 11 == 0
