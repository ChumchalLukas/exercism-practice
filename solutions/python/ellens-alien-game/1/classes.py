"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    # count of aliens

    total_aliens_created = 0

    
    # initialization
    def __init__(self, x, y):

        self.x_coordinate = x
        self.y_coordinate = y
        self.health = 3

        Alien.total_aliens_created += 1

    # hit method

    def hit(self):

        self.health -= 1

    # alive

    def is_alive(self):

        return False if self.health <= 0 else True

    # teleport

    def teleport(self, x, y):

        self.x_coordinate = x
        self.y_coordinate = y

    # collision

    def collision_detection(self, other_object):

        # Collision detection - condition for hit
        condition = (self.x_coordinate == other_object.x_coordinate) and (self.y_coordinate == other_object.y_coordinate)

        if condition:
            return True

        return None

        

        
        


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.

def new_aliens_collection(coordinates):
    """Return a list of Alien objects created from a list of (x, y) coordinates."""
    return [Alien(x, y) for x, y in coordinates]

