"""
score.py

* counts the scores for each H-connection
* counts the scores for each C-connection (if present)
* gives a total score for each fold
* compares total scores of different proteins to determine the optimal fold
"""

from .fold import Fold

class Score:
    """
    Collection of all functions regarding the score.
    * calculate_score() = calculates score of a Fold
    * get_neighbour_obj() = gets a neighbour object from a given coordinate
    * check_surrounding_coordinates() = retrieves surrounding coordinates of given coordinate
    * best_fold() = determines the best fold of a given list, based on the score
    """

    def __init__(self):
        """
        Initializes Scoring object
        """
        pass


    def calculate_score(self, Fold) -> int:
        """
        Function loops over the existing list of used coordinates to see if the
        given coordinate of an H aminoacid sides another H, if so, -1 is added to the score.
        If the given coordinate of a C aminoacid sides another C, -5 is added to score.

        Parameters:
        -----
        self = Score object
        Fold = the current fold to be scored
        
        Output:
        -----
        score = the score calculated for the given Fold
        """
        # set score to 0
        score = 0
        
        # loop over all aminoacids
        for Aminoacid in Fold.aminoacids:
            # for H aminoacids, get neighbours (surrounding aminoacids)
            if Aminoacid.aminotype == 'H':
                neighbours = self.check_surrounding_coordinates(Aminoacid.coordinate, Fold)
                # for each neighbour, check if it is also an H aminoacid
                for neighbour in neighbours:
                    neighbour_obj = self.get_neighbour_obj(neighbour, Fold)
                    if neighbour_obj.aminotype == 'H' or neighbour_obj.aminotype == 'C':
                        # if both H aminoacids are not already connected or counted, add -1 for H-bond
                        if neighbour_obj.id >= Aminoacid.id + 2:
                            score -= 1
                            
            # for C aminoacids, get neighbours (surrounding aminoacids)
            elif Aminoacid.aminotype == 'C':
                neighbours = self.check_surrounding_coordinates(Aminoacid.coordinate, Fold)
                # for each neighbour, check if it is also a C aminoacid
                for neighbour in neighbours:
                    neighbour_obj = self.get_neighbour_obj(neighbour, Fold)
                    if neighbour_obj.aminotype == 'C':
                        # if both C aminoacids are not already connected or counted, add -5 for C-bond
                        if neighbour_obj.id >= Aminoacid.id + 2:
                            score -= 5      
                    elif neighbour_obj.aminotype == 'H':
                        if neighbour_obj.id >= Aminoacid.id + 2:
                            score -= 1

        return score
    
    def get_neighbour_obj(self, coordinate, Fold):
        """
        Determine the corresponding Fold object of the coordinate
        
        Parameters:
        ----
        self = Score object
        coordinate = the coordinate of the desired Aminoacid object
        Fold = the fold containing the relevant Aminoacids and their coordinates
        """
        ind = Fold.coordinates.index(coordinate)
        neighbour_obj = Fold.aminoacids[ind]
        
        return neighbour_obj


    def check_surrounding_coordinates(self, current_coordinate, Fold) -> list:
        """
        Gets coordinate and checks the surrounding coordinates.

        Parameters:
        -----
        self = Score object
        current_coordinate = coordinate whose neighbours are needed
        Fold = the Fold containing the relevant Aminoacids
        
        Output:
        -----
        neighbours = a list of coordinates that gives the
        (Von-Neumann) neighbours of the current_coordinate
        """
        # create neighbour list
        neighbours = []
        # get x and y of current coordinate
        current_x = current_coordinate[0]
        current_y = current_coordinate[1]
        
        # loop over coordinates of aminoacids in Fold
        for coordinate in Fold.coordinates:
            x = coordinate[0]
            y = coordinate[1]
            
            # if coordinate surrounding current coordinate, add to neighbours
            if current_x + 1 == x and current_y == y:
                neighbours.append(coordinate)
            elif current_x - 1 == x and current_y == y:
                neighbours.append(coordinate)
            elif current_y + 1 == y and current_x == x:
                neighbours.append(coordinate)
            elif current_y - 1 == y and current_x == x:
                neighbours.append(coordinate)
            
        return neighbours


    def best_fold(self, valid_folds: list) -> object:
        """
        Function checks all the scores of the made folds and picks the fold with the best score.

        Parameters:
        -----
        valid_folds = list of completed folds
        
        Output:
        -----
        best_fold = Fold object with best score
        """

        max_score = 0
        best_fold = None
        
        # loop over folds
        for fold in valid_folds:
            # determine score for Fold
            score = self.calculate_score(fold)
            fold.store_score(score)
            # if score lower than best score, assign new best fold
            if fold.score < max_score:
                max_score = fold.score
                best_fold = fold

        return best_fold
    
    def calculate_score_monte_carlo(self, Elongation):
        """Function loops over the list of coordinates in the elongation object and calculates the score
        by checking if there are non covalent bound H's next to eachother (-1 point) or if there are 
        non-covalent bound C's next to eachother (-5)."""
         # set score to 0
        score = 0
        
        # loop over all aminoacids
        for Aminoacid in Elongation.aminoacids:
            # for H aminoacids, get neighbours (surrounding aminoacids)
            if Aminoacid.aminotype == 'H':
                neighbours = self.check_surrounding_coordinates(Aminoacid.coordinate, Elongation)
                # for each neighbour, check if it is also an H aminoacid
                for neighbour in neighbours:
                    neighbour_obj = self.get_neighbour_obj(neighbour, Elongation)
                    if neighbour_obj.aminotype == 'H':
                        # if both H aminoacids are not already connected or counted, add -1 for H-bond
                        if neighbour_obj.id >= Aminoacid.id + 2:
                            score -= 1
                            
            # for C aminoacids, get neighbours (surrounding aminoacids)
            elif Aminoacid.aminotype == 'C':
                neighbours = self.check_surrounding_coordinates(Aminoacid.coordinate, Elongation)
                # for each neighbour, check if it is also a C aminoacid
                for neighbour in neighbours:
                    neighbour_obj = self.get_neighbour_obj(neighbour, Elongation)
                    for neighbour in neighbours:
                        if neighbour_obj.aminotype == 'C':
                            # if both C aminoacids are not already connected or counted, add -5 for C-bond
                            if neighbour_obj.id >= Aminoacid.id + 2:
                                score -= 5 

        return score 
