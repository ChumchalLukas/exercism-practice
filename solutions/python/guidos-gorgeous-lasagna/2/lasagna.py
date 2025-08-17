"""
Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# Define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40

# Define the 'PREPARATION_TIME' constant.
PREPARATION_TIME = 2

def bake_time_remaining(baked: int) -> int:
    """Calculate the bake time remaining.

    :param baked: int - time in minutes the lasagna has been baking
    :return: int - remaining bake time derived from EXPECTED_BAKE_TIME
    """
    return EXPECTED_BAKE_TIME - baked

def preparation_time_in_minutes(layer: int) -> int:
    """Calculate the preparation time.

    :param layer: int - number of layers in the lasagna
    :return: int - total preparation time
    """
    return layer * PREPARATION_TIME

def elapsed_time_in_minutes(layer: int, cooktime: int) -> int:
    """Calculate the total elapsed cooking time.

    :param layer: int - number of lasagna layers
    :param cooktime: int - baking time in minutes
    :return: int - total elapsed cooking time in minutes
    """
    layer_assembly = layer * PREPARATION_TIME
    return layer_assembly + cooktime
