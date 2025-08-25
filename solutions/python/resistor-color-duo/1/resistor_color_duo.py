
_COLORS = {
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


def value(colors:list) -> int:
    """
    Returning type of two rasberry pi resistors
    """

    resistor1 = _COLORS[colors[0]]
    resistor2 = _COLORS[colors[1]]

    return int(str(resistor1) + str(resistor2))