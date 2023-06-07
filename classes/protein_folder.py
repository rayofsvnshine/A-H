"""
protein_folder.py

------
* folds protein according to certain criteria:
    * no overlap on 2D grid
    * folds are done with 90 degree angles
    * check if the next space allows further movement
    * if movement is stunted, invalid fold
* fold 
* stores coordinates of aminoacids
* checks for hydrophobic aminoacids (H) if there are other H's around (without covalent binding)
    * if there is an H around, calls scoring class to keep track of score 
"""

from random import choice
# import numpy as np
from classes.folded_protein import Fold
from classes.scoring import Score

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
        self.Grid = self.make_grid()
        self.Folds = self.make_folds()
        self.Best_fold = self.find_best_fold()
        
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
        
    def fold_protein(self) -> (Fold | None):
        """
        Attempts to fold the protein
        
        Returns:
        -----
        None = if an invalid fold is created
        
        Fold = a Fold object with a valid fold
        """
        # needs to return a fold
            
        # make grid and set starting point
        grid = self.make_grid()
        starting_point = (0,0)
        
        # make list for coordinates
        coordinates = [(0,0)]
        
        # put aminoacids down until end of protein
        for aminoacid in self.Protein.length:
            options = self.check_directions(starting_point)
            if options == None:
                return None
            starting_point = choice(options)
            coordinates.append(starting_point)
            
        # if fold was completed, return
        new_fold = Fold(coordinates)
        return new_fold
            
            
    def find_best_fold(self) -> Fold:
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
            
    def make_grid(self) -> list:
        """
        Creates a grid with coordinates according to the size of self.Protein.
        The x-axis and y-axis extend in positive and negative direction
        as far as the length of the protein.
        
        Returns:
        -----
        gridspace = list of lists with coordinate tuples
        """
        # makes (an ugly:( ) grid
        gridspace = []
        gridsize = range(-(len(self.Protein.length)), (len(self.Protein.length) + 1))
        index_counter = 0
        for y in gridsize:
            gridspace.append([])
            for x in gridsize:
                coordinate = ((y), (x))
                gridspace[index_counter].append(coordinate)
            index_counter += 1
            
        return gridspace
            
    def check_direction(self, starting_point) -> tuple:
        """
        Determines the coordinate where the following aminoacid will be placed.
        
        Parameters:
        -----
        starting_point = previous coordinate
        
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
        next_point = ((x + 1), y)
        return next_point
    
    def place_aminoacid(self, coordinate):
        pass
        


"""
This is to test out the different grid functions
"""
# if __name__ == "__main__":
    
    # gridspace = []
    # gridsize = range(-5, 6)
    # i = 0
    # for y in gridsize:
    #     gridspace.append([])
    #     for x in gridsize:
    #         coordinate = ((y), (x))
    #         gridspace[i].append(coordinate)
    #     i += 1
    
    # new_grid = np.array(gridspace)
    
    # line = np.linspace(-5,5, 11)
    # new_grid = np.meshgrid(line, indexing="xy")
    # new_grid = np.array(line)
    
    # grid = new_grid
    # print(grid)