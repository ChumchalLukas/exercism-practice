def color_code(color):

    """
    Return resistor value according it´s color for rasberry pi
    
    """

    resistor_colors = {
        "black" : 0,
        "brown" : 1,
        "red" : 2,
        "orange" : 3,
        "yellow" : 4,
        "green" : 5,
        "blue" : 6,
        "violet" : 7,
        "grey" : 8,
        "white" : 9
    }

    return resistor_colors[color]


def colors():

    """
    Procedure listing all resistors collors 0 -> 9
    
    """

    resistor_colors_order = ["black", "brown", "red", "orange", 
                             "yellow", "green", "blue", "violet",
                             "grey", "white"]

    return resistor_colors_order
