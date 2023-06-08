from protein_folder import Folder
from folded_protein import Fold

class Score:
    """
    Parameters:
    -------
    List of tuples with directions

    Returns:
    -------
    CSV with optimal protein coordinates (tuples) and score

    -------
    * counts the scores for each H-connection
    * counts the scores for each C-connection (if present)
    * gives a total score for each fold
    * compares total scores of different proteins to determine the optimal fold
    """
    def __init__(self, coordinates):
        """Initializer"""
        self.coordinates = coordinates

    def calculate_score(coordinates):
        """ Function loops over the existing list of used coordinates to see if the
        given coordinate of the H aminoacid sides another H, if so, -1 is added to the score.
        Returns the score retrieved from this aminoacid."""
        score = 0
        last_coordinate = None
        current_coordinate = None
        next_coordinate = None
        index = 0
        for coordinate, index in coordinates:
            current_coordinate = coordinate
            for n_coordinate + 1 in coordinates:
                next_coordinate = n_coordinate
                if index != 0:
                    if last_coordinate[0] > current_coordinate[0]:  # hij komt van rechts
                        if next_coordinate[0] < current_coordinate[0]: # hij gaat naar rechts
                            if current_coordinate[1] + 1 in coordinates:
                                score += -1
                            if current_coordinate[1] - 1 in coordinates:
                                score += -1
                        if next_coordinate[1] > current_coordinate[1]: # hij gaat naar beneden
                            if current_coordinates[0] + 1 in coordinates:
                                score += -1
                            if current_coordinate[1] + 1 in coordinates:
                                score += -1
                        if next_coordinate[1] < current_coordinate[1]: # hij gaat naar beneden
                            if current_coordinate[0] + 1 in coordinates:
                                score += -1
                            if current_coordinate[1] + 1 in coordinates

                    if last_coordinate[0] < current_coordinate[0]: # hij komt van links
                        if next_coordinate[0] > current_coordinate[0]: # hij gaat naar links
                            if current_coordinates[1] - 1 in coordinates:
                                score += -1
                            if current_coordinates[1] + 1 in coordinates:
                                score += -1 
                        if next_coordinate[1] > current_coordinate[1]: # hij gaat naar beneden
                            if current_coordinates[0] + 1 in coordinates:
                                score += -1
                        if next_coordinate[1] < current_coordinate[1]: # hij gaat naar boven
                            if current_coordinates[0] + 1 in coordinates:
                                score += -1

                    if last_coordinate[1] > current_coordinate [1]: # hij komt van onder
                        if next_coordinate[0] < current_coordinate[0]:
                        if next_coordinate[0] > current_coordinate[0]:
                        if next_coordinate[1] < current_coordinate[1]:

                    if last_coordinate[1] < current_coordinate [1]: # hij komt van boven
                        if next_coordinate[0] < current_coordinate[0]:
                        if next_coordinate[0] > current_coordinate[0]:
                        if next_coordinate[1] > current_coordinate[1]:
            else:
                continue

        last_coordinate = coordinate

        return score

    def best_fold(valid_folds):
        """ Function checks all the scores of the made folds and picks the fold with the best score."""
        max_score = 0
        for fold in valid_folds:
            if fold.score > max_score:
                max_score = fold.score

        return max_score
