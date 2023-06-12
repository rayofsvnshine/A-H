"""
score.py

* counts the scores for each H-connection
* counts the scores for each C-connection (if present)
* gives a total score for each fold
* compares total scores of different proteins to determine the optimal fold
"""

from .fold import Fold
from .aminoacid import Aminoacid

class Score:
    """
    Collection of all functions regarding the score.
    """

    def __init__(self, coordinates):
        """
        Initializer
        """

        self.coordinates = coordinates


    def calculate_score(self, Fold) -> int:
        """
        Function loops over the existing list of used coordinates to see if the
        given coordinate of the H aminoacid sides another H, if so, -1 is added to the score.

        Pre:
            ...
        Post:
            Returns the score retrieved from this aminoacid.
        """

        score = 0
        teller = 0 
        index = Fold.aminoacids[1].id
        for Aminoacid in Fold.aminoacids:
            neighbours = self.check_surrounding_coordinates(Aminoacid.coordinate, Fold)

            for neighbour in neighbours:
                if neighbour in Fold.coordinates:
                    if Aminoacid.aminotype == 'H':
                        neighbour_obj = self.get_neighbour_obj(neighbour, Fold)
                        if neighbour_obj.aminotype == 'H':
                            if neighbour_obj.id + 1 != Aminoacid.id | neighbour_obj.id - 1 != Aminoacid.id:
                                score -= 1
                                print(neighbour_obj.id, Aminoacid.id)
                    elif Aminoacid.aminotype == 'C':
                        neighbour_obj = self.get_neighbour_obj(neighbour, Fold)
                        if neighbour_obj.aminotype == 'C':
                            if neighbour_obj.id + 1 != Aminoacid.id | neighbour_obj.id - 1 != Aminoacid.id:
                              score -= 5      
            index += 1
            teller += 1
        return score
    
    def get_neighbour_obj(self, coordinate, Fold):
        ind = Fold.coordinates.index(coordinate)
        neighbour_obj = Fold.aminoacids[ind]
        return neighbour_obj


    def check_surrounding_coordinates(self, current_coordinate, Fold) -> list:
        """
        Gets coordinate and checks the surrounding coordinates.

        Pre:
            ...
        Post:
            ...
        """

        neighbours = []
        for coordinate in Fold.coordinates:
            # new code adjusted for x/y
            x = coordinate[0]
            y = coordinate[1]
            current_x = current_coordinate[0]
            current_y = current_coordinate[1]
            if current_x + 1 == x:
                neighbours.append(coordinate)
            elif current_x - 1 == x:
                neighbours.append(coordinate)
            elif current_y + 1 == y:
                neighbours.append(coordinate)
            elif current_y - 1 == y:
                neighbours.append(coordinate)
            
            # old code
            # if current_coordinate[0] + 1 == coordinate:
            #     neighbours.append(coordinate)
            # elif current_coordinate[0] - 1 == coordinate:
            #     neighbours.append(coordinate)
            # elif current_coordinate[1] + 1 == coordinate:
            #     neighbours.append(coordinate)
            # elif current_coordinate[1] - 1 == coordinate:
            #     neighbours.append(coordinate)

        return neighbours


    def best_fold(valid_folds) -> int:
        """
        Function checks all the scores of the made folds and picks the fold with the best score.

        Pre:
            ...
        Post:
            ...
        """

        max_score = 0
        best_fold = 0
        for fold in valid_folds:
            if fold.score < max_score:
                max_score = fold.score
                best_fold = fold

        return best_fold
