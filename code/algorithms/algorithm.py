"""
algorithm.py

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
from ..classes.score import Score
from ..classes.aminoacid import Aminoacid

class Folder(object):
    """
    Creates a Folder object that can:
    * create randomly generated folds for a given protein
    * compare folds to one another
    * determine the best generated Fold
    """

    def __init__(self, Protein: object):
        """
        Initializes a Folder object
        
        Parameters:
        ----
        Protein = Protein object with properties of a given protein
        
        Returns?:
        ----
        self.Best_fold = the optimal generated fold of a protein with coordinates and score
        """
        self.Protein = Protein
        self.amino_counter = 0
        self.fold_counter = 0
        self.Folds = self.make_folds()
        
        
    def make_folds(self) -> list:
        """
        Creates folds until certain number of folds is reached
        
        Returns:
        ------
        a list of Fold objects
        """
        # stop making folds after 5 valid folds are found
        valid_folds = []
        
        while len(valid_folds) < 4:
            new_fold = self.fold_protein()
            if new_fold == None:
                continue
            valid_folds.append(new_fold)
            
        return valid_folds
        
    def fold_protein(self):
        """
        Attempts to fold the protein
        
        Returns:
        -----
        None = if an invalid fold is created
        
        Fold = a Fold object with a valid fold
        """
        # needs to return a fold
            
        # make grid and set starting point
        # grid = self.make_grid()
        starting_point = (0,0)
        # fold_score = 0
        
        # make list for coordinates and aminoacids
        coordinates = []
        directions = []
        amino_list = []
        amino_amigos = self.Protein.protein
        previous_coordinate = None
        # previous_amino = None
        
        # put aminoacids down until end of protein
        for aminoacid in amino_amigos:
            coordinates.append(starting_point) # store coordinate
            options = self.check_directions(starting_point, coordinates)
            if options == []:
                return None
            
            # create aminoacid to use
            new_amino = Aminoacid(self.amino_counter, aminoacid)
            amino_list.append(new_amino)
            self.amino_counter += 1
         
            # reassign starting point and append to coordinate list
            new_amino.set_previous_coordinate(previous_coordinate) # set origin direction
            new_amino.store_coordinates(starting_point)
            starting_point, direction = self.choose_direction(starting_point, options)
            new_amino.set_next_direction(starting_point)
            
            
            # store coordinates and directions
            directions.append(direction) # store direction
            previous_coordinate = starting_point
            
        # if fold was completed, return
        new_fold = Fold(self.fold_counter, amino_list, coordinates, directions)
        # create scoring object (maybe put this somewhere else??)
        # score_obj = Score()
        # fold_score = score_obj.calculate_score(new_fold)
        # new_fold.store_score(fold_score)
        self.fold_counter += 1
        
        return new_fold
            
            
    # def find_best_fold(self) -> object:
    #     """
    #     Looks at each fold and calculates the score
        
    #     Returns:
    #     -----
    #     best_fold = Fold object with highest Score attribute
    #     """
    #     # calculate score per fold
    #     for current_fold in self.Folds:
    #         score = Score.calculate_score(current_fold)
    #         current_fold.store_score(score)
    #     # find best fold and return
    #     best_fold = Score.best_fold(self.Folds)
        
    #     return best_fold
            
    # def make_grid(self) -> list:
    #     """
    #     Creates a grid with coordinates according to the size of self.Protein.
    #     The x-axis and y-axis extend in positive and negative direction
    #     as far as the length of the protein.
        
    #     Returns:
    #     -----
    #     gridspace = list of lists with coordinate tuples
    #     """
    #     # makes grid
    #     gridspace = []
    #     gridsize = range(-(len(self.Protein.length)), (len(self.Protein.length) + 1))
    #     for y in gridsize:
    #         for x in gridsize:
    #             coordinate = ((y), (x))
    #             gridspace.append(coordinate)
            
    #     return gridspace
            
    def check_directions(self, starting_point, coordinates) -> list:
        """
        Determines the coordinate where the following aminoacid will be placed.
        
        Parameters:
        -----
        starting_point = previous coordinate
        coordinates = previous route
        
        Returns:
        -----
        options = list with possible coordinates
        """
        # returns list of possible coordinates
        orientations = [(0,1), (0,-1), (1,0), (-1,0)]
        options = []
        
        for plus_x, plus_y in orientations:
            x, y = starting_point
            new_x = x + plus_x
            new_y = y + plus_y
            if (new_x, new_y) in coordinates:
                continue
            else:
                options.append(((new_x), (new_y)))
                
        return options
    
    def choose_direction(self, starting_point, options):
        next_point = choice(options)
        # if there's a difference in y-coordinate, direction is -2 or 2
        if starting_point[0] == next_point[0]:
            # calculate if movement is in positive or negative direction
            direction = next_point[1] - starting_point[1]
            direction = 2 * direction
        # if there's a difference in x-coordinate, direction is -1 or 1
        elif starting_point[1] == next_point[1]:
            # calculate if movement is in positive or negative direction
            direction = next_point[0] - starting_point[0]    
            
        return next_point, direction
            