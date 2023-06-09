"""
aminoacid.py

* ...

Pre:
    Stores all properties of a aminoacod.
Post:
    Properties of the folded protein.
"""

class Aminoacid(object):
    """Aminoacid object"""

    def __init__(self, amino_id, aminotype):
        """
        Initializer
        """

        self.amino_id = id
        self.aminotype = aminotype


    def set_origin_direction(self, direction):
        """..."""

        self.origin_direction = direction


    def set_target_direction(self, direction):
        """..."""

        self.target_direction = direction


    def store_coordinates(self, coordinate):
        """Gets the type of aminoacid (H, P, C) and the coordinates and stores them together."""

        self.coordinate = coordinate
