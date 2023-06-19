"""
fold.py

* Stores all properties of the folded protein
"""

class Fold(object):
    """
    Fold object
    """

    def __init__(self, id: int, aminoacids: list, coordinates: list, directions: list):
        """
        Initializer
        """

        self.id = id
        self.aminoacids = aminoacids
        self.coordinates = coordinates
        self.directions = directions
        self.results = []
        self.store_results()


    def store_results(self) -> None:
        """
        Makes list with aminoacids and directions.
        
        Pre:
            ...
        Post:
            ...
        """

        for i in range(len(self.aminoacids)):
            self.results.append((self.aminoacids[i].aminotype, self.directions[i]))


    def store_score(self, protein_score: int) -> None:
        """
        Gets the score of a fold to store it in the fold object.

        Pre:
            ...
        Post:
            ...
        """

        self.score = protein_score
        
    
    def add_amino(self, aminoacid, coordinate, direction):
        self.aminoacids.append(aminoacid)
        self.coordinates.append(coordinate)
        self.directions.append(direction)
        
    def add_score(self, score):
        self.score += score
