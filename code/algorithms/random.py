"""
random.py
Ray Pelupessy

* folds protein according to certain criteria:
    * no overlap on 2D grid.
    * folds are done with 90 degree angles.
    * check if the next space allows further movement.
    * if movement is stunted, invalid fold.
* fold
* stores coordinates of aminoacids.
* checks for hydrophobic aminoacids (H) if there are other H's around (without covalent binding):
    * if there is an H around, calls scoring class to keep track of score.
"""

from random import choice
from ..classes.fold import Fold
from ..classes.aminoacid import Aminoacid
from ..classes.score import Score

class Random(object):
    """
    Creates a Folder object that can:
    * create randomly generated folds for a given protein
    * compare folds to one another
    * determine the best generated Fold
    """

    def __init__(self, Protein: object, number_of_runs: int):
        """
        Initializes a Folder object
        
        Parameters:
        ----
        Protein = Protein object with properties of a given protein
        number_of_runs = the amount of times to run the algorithm
        """
        self.Protein = Protein
        self.amino_counter = 0
        self.fold_counter = 0
        self.Score = Score()
        self.Folds = self.make_folds(number_of_runs)
        
        
    def make_folds(self, number_of_runs: int) -> list:
        """
        Creates folds until certain number of folds is reached
        
        Parameters:
        ----
        number_of_runs = how many times the algorithm needs to run
        
        Output:
        ------
        valid_folds = a list of Fold objects
        """
        # stop making folds after number_of_runs are folded
        valid_folds = []
        while len(valid_folds) < number_of_runs:
            new_fold = self.fold_protein()
            if new_fold == None:
                continue
            fold_score = self.Score.calculate_score(new_fold)
            new_fold.store_score(fold_score)
            valid_folds.append(new_fold)
            
        return valid_folds
    
        
    def fold_protein(self) -> object:
        """
        Attempts to fold the protein
        
        Output:
        -----
        None = if an invalid fold is created
        new_fold = a Fold object with a valid fold
        """ 
        # set starting point
        starting_point = (0,0)
        
        # make list for coordinates and aminoacids
        coordinates = []
        amino_list = []
        # get all aminoacids in Protein
        amino_amigos = self.Protein.protein
        # set previous coordinate
        previous_coordinate = None
        
        # put aminoacids down until end of protein
        for aminoacid in amino_amigos:
            # determine next possible coordinates
            options = self.check_directions(starting_point, coordinates)
            # if no next possible steps, return None for incomplete fold
            if options == []:
                return None
            
            # create aminoacid to use
            new_amino = Aminoacid(self.amino_counter, aminoacid)
            amino_list.append(new_amino)
            self.amino_counter += 1
         
            # store aminoacid's current position in coordinate list and object
            coordinates.append(starting_point)
            new_amino.set_current_coordinate(starting_point)
            # set aminoacid's previous coordinate
            new_amino.set_previous_coordinate(previous_coordinate)
            # decide direction and next point of aminoacid chain
            starting_point = self.choose_direction(options)
            # save next direction in aminoacid
            new_amino.set_next_coordinate(starting_point)
            
            # store direction and change previous coordinate to current coordinate
            previous_coordinate = starting_point
            
        # if fold was completed, store in Fold object
        new_fold = Fold(self.fold_counter, self.Protein.protein, amino_list, coordinates)
        self.fold_counter += 1
        
        return new_fold
    
            
    def check_directions(self, starting_point: tuple, coordinates: list) -> list:
        """
        Determines the coordinate where the following aminoacid will be placed.
        
        Parameters:
        -----
        starting_point = previous coordinate
        coordinates = all coordinates where there are already Aminoacids
        
        Returns:
        -----
        options = list with possible coordinates
        """
        orientations = [(0,1), (0,-1), (1,0), (-1,0)]
        options = []
        
        # for each direction, check if it has already been visited or not and append if not
        for plus_x, plus_y in orientations:
            x, y = starting_point
            new_x = x + plus_x
            new_y = y + plus_y
            if (new_x, new_y) in coordinates:
                continue
            else:
                options.append(((new_x), (new_y)))
                
        return options
    
    
    def choose_direction(self, options: list) -> tuple:
        """
        returns a randomly chosen coordinate from list
        
        Parameters:
        ----
        options = list of possible coordinates
        
        Output:
        ----
        next_point = tuple containing the next coordinate of the fold
        """
        next_point = choice(options) 
            
        return next_point
            