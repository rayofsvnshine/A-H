class Fold(object):
    """

    Parameters:
    ------
    Fold class
    ------
    Stores all used coordinates and the score of the fold. 

    Returns:
    ------
    Properties of the folded protein
    * coordinates of animoacids
    * score of fold

    """

    def __init__(self, score):
        """ Initializer"""
        self.coordinates = []
        self.scores = score


    def store_coordinates(self, coordinates, a_type):
        """Gets the type of aminoacid (H, P, C) and the coordinates and stores them together"""
        for coordinate in coordinates:
            self.coordinates.append(coordinate)


    def store_score(self, protein_score):
        """Gets the score of a fold to store it in the fold object."""
        self.score = protein_score
