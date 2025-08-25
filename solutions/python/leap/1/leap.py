def leap_year(year):

    # Even leap year
    if year % 4 == 0:
        if (year % 100 == 0) and (year % 400 == 0):
            return True
        elif (year % 100 == 0) and not(year % 400 == 0):
            return False
        return True

    # Every other year
    if year % 4 != 0:
        return False
