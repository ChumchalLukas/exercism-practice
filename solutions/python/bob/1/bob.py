def response(hey_bob):
    
    stripped = hey_bob.strip()
    
   
    if not stripped:
        return "Fine. Be that way!"
    
    
    is_question = stripped.endswith("?")
    is_yelling = stripped.isupper()
    
    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return "Sure."
    elif is_yelling:
        return "Whoa, chill out!"
    else:
        return "Whatever."

