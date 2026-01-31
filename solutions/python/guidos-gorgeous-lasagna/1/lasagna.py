"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.

EXPECTED_BAKE_TIME = 40


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(baked:int) -> int:
    """Calculate the bake time remaining.

    baked:int - time in minutes of baking
    return Int → time needed to wait to fully baked the lasana

    This function take baked as expected time in minutes and substract it from 
    EXPECTED_BAKE_TIME to get time to wait.
    
    """

    return EXPECTED_BAKE_TIME - baked


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.

PREPARATION_TIME = 2

def preparation_time_in_minutes(layer:int) -> int:
    """
    layer: int - counts of layers of lasagna

    return preparation time of all layers  by multipling counts of layers by PREPARATION_TIME 
    
    """

    
    return layer*PREPARATION_TIME


#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)

def elapsed_time_in_minutes(layer:int, cooktime:int) -> int:

    """
    Function: total time took of cooking as int of minutes

    layer: counts of layers in lasagna
    cooktime: time of lasagna already cooked
    
    
    """

    layer_assembly = layer * PREPARATION_TIME

    return layer_assembly + cooktime

