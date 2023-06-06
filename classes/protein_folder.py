"""
protein_folder.py
Folder class

Parameters:
------
Protein chain (String)

Returns:
------
Various folds of the protein chain
List of tuples with directions

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
# import Fold

class Folder:

    def __init__(self, Protein):
        self.Protein = Protein
        self.Grid = self.make_grid()
        
    def make_folds(self):
        # stop making folds after 5 valid folds are found
        valid_folds = []
        
        while len(valid_folds) < 4:
            new_fold = self.fold_protein()
            valid_folds.append(new_fold)
        
    def fold_protein(self):
        # needs to return a fold
            
        # make grid
        starting_point = (0,0)
        # put aminoacids down until end of protein
        for aminoacid in self.Protein.length:
            options = self.check_directions(starting_point)
            starting_point = choice(options)
            
    def make_grid(self):
        gridspace = []
        for y in len(self.Protein.length):
            gridspace.append([])
            for x in len(self.Protein.length):
                coordinate = ((0 - y), (0 - x))
                gridspace[y].append(coordinate)
            
    def check_direction(self, starting_point):
        # checks which directions line can go
        # returns list of possible coordinates
        pass
