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
# import numpy as np
from .aminoacid import Fold
from .score import Score

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
        
        # make list for coordinates
        coordinates = [(0,0)]
        directions = []
        
        # put aminoacids down until end of protein
        for aminoacid in self.Protein.length:
            options = self.check_directions(starting_point, coordinates)
            if options == None:
                return None
            
            # reassign starting point and append to coordinate list
            starting_point, direction = self.choose_direction(starting_point, options)
            coordinates.append(starting_point)
            directions.append(direction)
            
        # if fold was completed, return
        new_fold = Fold(coordinates, directions)
        return new_fold
            
            
    def find_best_fold(self) -> object:
        """
        Looks at each fold and calculates the score
        
        Returns:
        -----
        best_fold = Fold object with highest Score attribute
        """
        # calculate score per fold
        for current_fold in self.Folds:
            score = Score.calculate_score(current_fold)
            current_fold.store_score(score)
        # find best fold and return
        best_fold = Score.best_fold(self.Folds)
        
        return best_fold
            
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
            
    def check_direction(self, starting_point, coordinates) -> tuple:
        """
        Determines the coordinate where the following aminoacid will be placed.
        
        Parameters:
        -----
        starting_point = previous coordinate
        coordinates = previous route
        
        Returns:
        -----
        next_point = tuple with coordinates
        """
        
        # things it should do:
        # checks which directions line can go
        # returns list of possible coordinates
        # if no options possible, return None
        
        # goes to the coordinate right to the previous point
        x, y = starting_point
        # orientations = ["up", "down", "right", "left"]
        
        
        next_point = ((x + 1), y)
        
        if next_point in coordinates:
            # move on to next option
            pass
        
        return next_point
    
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
            


"""
This is to test out the different grid functions
"""
# if __name__ == "__main__":
    
#     gridspace = []
#     gridsize = range(-5, 6)
#     for y in gridsize:
#         for x in gridsize:
#             coordinate = ((y), (x))
#             gridspace.append(coordinate)
    
    # new_grid = np.array(gridspace)
    
    # line = np.linspace(-5,5, 11)
    # new_grid = np.meshgrid(line, indexing="xy")
    # new_grid = np.array(line)
    
    # grid = gridspace
    # print(grid)
