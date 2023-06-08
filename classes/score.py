"""
scoring.py

* counts the scores for each H-connection
* counts the scores for each C-connection (if present)
* gives a total score for each fold
* compares total scores of different proteins to determine the optimal fold

Pre:
    Uses a list of tuples with directions.
Post:
    Returns a int score for the optimal protein folding steps.
"""

from .algorithm import Folder
from .aminoacid import Fold

class Score:
    """Collection of all functions regarding the score."""


    def __init__(self, coordinates):
        """Initializer"""

        self.coordinates = coordinates


    def select_only_H(coordinatesandtype):
        """
        Function makes list of all the coordinates that are occupied by H aminoacids.

        Pre:
            ...
        Post:
            Returns a list of only the H coordinates.
        """

        only_H = []

        for i in coordinatesandtype:
            if coordinatesandtype.values[i] == "H":
                    only_H.append(coordinates.keys[i])

        return only_H


    def calculate_score(self, coordinates):
        """
        Function loops over the existing list of used coordinates to see if the
        given coordinate of the H aminoacid sides another H, if so, -1 is added to the score.

        Pre:
            ...
        Post:
            Returns the score retrieved from this aminoacid.
        """

        score = 0
        last_coordinate = None
        current_coordinate = None
        next_coordinate = None
        index = range(len(coordinates) - 1)

        for i in index:
            current_coordinate = coordinates[i]
            next_coordinate = coordinates[i + 1]

            if index != 0 and index != 1:
                if last_coordinate[0] > current_coordinate[0]:  # hij komt van rechts
                    if next_coordinate[0] < current_coordinate[0]: # hij gaat naar rechts
                        if current_coordinate[1] + 1 in coordinates:
                            score += -1
                        if current_coordinate[1] - 1 in coordinates:
                            score += -1

                    if next_coordinate[1] > current_coordinate[1]: # hij gaat naar beneden
                        if current_coordinate[0] + 1 in coordinates:
                            score += -1
                        if current_coordinate[1] + 1 in coordinates:
                            score += -1

                    if next_coordinate[1] < current_coordinate[1]: # hij gaat naar beneden
                        if current_coordinate[0] + 1 in coordinates:
                            score += -1
                        if current_coordinate[1] + 1 in coordinates:
                            score += -1


                if last_coordinate[0] < current_coordinate[0]: # hij komt van links
                    if next_coordinate[0] > current_coordinate[0]: # hij gaat naar links
                        if current_coordinate[1] - 1 in coordinates:
                            score += -1
                        if current_coordinate[1] + 1 in coordinates:
                            score += -1

                    if next_coordinate[1] > current_coordinate[1]: # hij gaat naar beneden
                        if current_coordinate[0] + 1 in coordinates:
                            score += -1
                        if current_coordinate[1] + 1 in coordinates:
                            score += -1

                    if next_coordinate[1] < current_coordinate[1]: # hij gaat naar boven
                        if current_coordinate[0] + 1 in coordinates:
                            score += -1
                        if current_coordinate[1] + 1 in coordinates:
                            score += -1


                if last_coordinate[1] > current_coordinate [1]: # hij komt van onder
                    if next_coordinate[0] < current_coordinate[0]: # hij gaat naar links
                        if current_coordinate[0] - 1 in coordinates:
                            score += -1
                        if current_coordinate[1] - 1 in coordinates:
                            score += -1

                    if next_coordinate[0] > current_coordinate[0]: # hij gaat naar rechts
                        if current_coordinate[0] - 1 in coordinates:
                            score += -1
                        if current_coordinate[1] + 1 in coordinates:
                            score += -1

                    if next_coordinate[1] < current_coordinate[1]: # hij gaat naar beneden
                        if current_coordinate[0] + 1 in coordinates:
                            score += -1
                        if current_coordinate[0] - 1 in coordinates:
                            score += -1


                if last_coordinate[1] < current_coordinate [1]: # hij komt van boven
                    if next_coordinate[0] > current_coordinate[0]: # hij gaat naar boven
                        if current_coordinate[0] + 1 in coordinates:
                            score += -1
                        if current_coordinate[0] - 1 in coordinates:
                            score += -1

                    if next_coordinate[1] < current_coordinate[1]: # hij gaat naar links
                        if current_coordinate[0] + 1 in coordinates:
                            score += -1
                        if current_coordinate[1] - 1 in coordinates:
                            score += -1

                    if next_coordinate[1] > current_coordinate[1]: # hij gaat naar rechts
                        if current_coordinate[0] - 1 in coordinates:
                            score += -1
                        if current_coordinate[1] - 1 in coordinates:
                            score += -1
            else:
                continue

            last_coordinate = current_coordinate

        # look at last coordinate
        current_coordinate = coordinates[-1]
        if last_coordinate[0] < current_coordinate[0]: # komt van rechts
            if current_coordinate[0] - 1 in coordinates:
                score += -1
            elif current_coordinate[1] + 1 in coordinates:
                score += -1
            elif current_coordinate[1] - 1 in coordinates:
                score += 1

        elif last_coordinate[1] < current_coordinate[1]: # komt van beneden
            if current_coordinate[1] + 1 in coordinates:
                score += -1
            elif current_coordinate[0] + 1 in coordinates:
                score += 1
            elif current_coordinate[0] - 1 in coordinates:
                score += 1

        elif last_coordinate[0] > current_coordinate[0]: # komt van links
            if current_coordinate[0] + 1 not in coordinates:
                score += -1
            if current_coordinate[0] - 1 in coordinates:
                score += -1
            elif current_score[1] + 1 in coordinates:
                score += -1
            elif current_score[1] - 1 in coordinates:
                score += -1
        elif last_coordinate[1] > current_coordinate[1]: # komt van boven
            if current_coordinate[1] + 1 not in coordinates:
                score += -1

        return score

    def best_fold(valid_folds):
        """ Function checks all the scores of the made folds and picks the fold with the best score."""
        max_score = 0
        for fold in valid_folds:
            if fold.score > max_score:
                max_score = fold.score

        return max_score
