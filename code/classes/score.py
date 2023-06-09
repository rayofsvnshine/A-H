"""
score.py

* counts the scores for each H-connection
* counts the scores for each C-connection (if present)
* gives a total score for each fold
* compares total scores of different proteins to determine the optimal fold

Pre:
    Uses a list of tuples with directions.
Post:
    Returns a int score for the optimal protein folding steps.
"""

from .fold import Fold
from .aminoacid import Aminoacid

class Score:
    """Collection of all functions regarding the score."""


    def __init__(self, coordinates):
        """Initializer"""

        self.coordinates = coordinates


    def calculate_score(self, Fold):
        """
        Function loops over the existing list of used coordinates to see if the
        given coordinate of the H aminoacid sides another H, if so, -1 is added to the score.

        Pre:
            ...
        Post:
            Returns the score retrieved from this aminoacid.
        """
        score = 0
        index = Fold.aminoacids[1].id
        for Aminoacid in Fold.aminoacids:
            neighbours = self.check_surrounding_coordinates(Aminoacid.coordinate, Fold)

            for neighbour in neighbours:
                if neighbour in Fold.coordinates:
                    if Aminoacid.type == 'H':
                        if neighbour.id + 1 != Aminoacid.id | neighbour.id -1 != Aminoacid.id:
                                score -= 1
            index += 1
        return score


    def check_surrounding_coordinates(self, current_coordinate, Fold):
        """ Gets coordinate and checks the surrounding coordinates """
        neighbours = []
        for coordinate in Fold.coordinates:
            if current_coordinate[0] + 1 == coordinate:
                neighbours.append(coordinate)
            elif current_coordinate[0] - 1 == coordinate:
                neighbours.append(coordinate)
            elif current_coordinate[1] + 1 == coordinate:
                neighbours.append(coordinate)
            elif current_coordinate[1] - 1 == coordinate:
                neighbours.append(coordinate)

        return neighbours


    def best_fold(valid_folds):
        """ Function checks all the scores of the made folds and picks the fold with the best score."""
        max_score = 0
        best_fold = 0
        for fold in valid_folds:
            if fold.score > max_score:
                max_score = fold.score
                best_fold = fold

        return best_fold
