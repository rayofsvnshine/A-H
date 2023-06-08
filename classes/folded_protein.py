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

    def __init__(self, score, coordinates):
        """
        Initializer
        ------
        self.coordinatesandtype = dict that stores coordinates and type of aminoacid.
        self.coordinates = list of all the used coordinates of the fold.
        self.scores = stores the score of the fold.
        """
        self.coordinatesandtype = {}
        self.coordinates = coordinates
        self.score = score


    def store_coordinates(self, coordinate, a_type):
        """Gets the type of aminoacid (H, P, C) and the coordinates and stores them together"""
        self.coordinatesandtype[coordinate].append(a_type)
        self.coordinates.append(coordinate)


    def store_score(self, protein_score):
        """Gets the score of a fold to store it in the fold object."""
        self.score = protein_score
