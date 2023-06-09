"""
aminoacid.py

* Stores all properties of an aminoacod
"""

class Aminoacid(object):
    """
    Aminoacid object
    """

    def __init__(self, id, aminotype):
        """
        Initializer
        """

        self.id = id
        self.aminotype = aminotype
        self.coordinate = ()


    def get_previous_coordinale(self, direction: tuple) -> None:
        """
        Sets the connection to previous amino acid.
        
        Pre:
            Direction is a tuple coordinate of the last amino acid.
        Post:
            Stores the previous direction.
        """

        self.origin_direction = direction


    def get_next_direction(self, direction: tuple) -> None:
        """
        Sets the connection to next amino acid.
        
        Pre:
            Direction is a tuple coordinate of the next amino acid.
        Post:
            Stores the next direction.
        """

        self.target_direction = direction


    def store_coordinates(self, coordinate: tuple) -> None:
        """
        Stores the coorinate of the amino acid.

        Pre:
            Coordinate is a tuple containing the coordinate of the amino acid.
        Post:
            Stores the coordinate of the amino acid.
        """

        self.coordinate = coordinate
