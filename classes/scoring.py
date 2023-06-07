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
    def __init__(self, current_coordinate):
        """Initializer"""
        self.current_coordinate = current_coordinate

    def calculate_score(current_coordinate, coordinates, last_chosen_direction):
        """ Function loops over the existing list of used coordinates to see if the
        given coordinate of the H aminoacid sides another H, if so, -1 is added to the score.
        Returns the score retrieved from this aminoacid."""
        score = 0
        for coordinate in coordinates:
            if "2" in last_chosen_direction:
                if coordinate == current_coordinate[0] - 1 || coordinate == current_coordinate[0] + 1:
                    score += -1
            if "1" in last_chosen_direction:
                if coordinate == current_coordinate[1] - 1 || coordinate == current_coordinate[1] + 1:
                    score += -1
        return score
    
