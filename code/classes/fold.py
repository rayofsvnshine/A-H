"""
folded_protein.py

* coordinates of animoacids
* score of fold

Pre:
    Stores all used coordinates and the score of the fold.
Post:
    Properties of the folded protein.
"""

class Fold(object):
    """Fold object"""

    def __init__(self, id: int, aminoacids: list, coordinates: list, directions: list):
        """
        Initializer
        """
        self.id = id
        self.aminoacids = aminoacids
        self.coordinates = coordinates
        self.directions = directions


    def store_score(self, protein_score):
        """Gets the score of a fold to store it in the fold object."""

        self.score = protein_score