"""Checking types of triangles according sides length:"""

def triangular_inequality(sides):
    """
    Checking triangular inequality:
    """

    a,b,c = sides

    inequality = (a + b > c) and (b + c > a) and (a + c > b)

    return inequality



def equilateral(sides):

    if triangular_inequality(sides):
        sides_set = set(sides)

        if len(sides_set) == 1:
            return True
        else:
            return False

    return False 


def isosceles(sides):
    
    if triangular_inequality(sides):
        sides_set = set(sides)

        if len(sides_set) <= 2:
            return True
        else:
            return False

    return False



def scalene(sides):

    if triangular_inequality(sides):
        sides_set = set(sides)

        if len(sides_set) == 3:
            return True
        else:
            return False

    return False

