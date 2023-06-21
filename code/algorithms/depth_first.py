"""
depth_first.py

runs a depth first algorithm to find optimal protein folds
"""

from ..classes.fold import Fold
from ..classes.aminoacid import Aminoacid
from ..classes.score import Score
import pickle
import os

class Depth_first(object):
    """
    Creates a Folder object that can:
    * create folds using a depth-first approach
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
        self.Score = Score()
        self.filename = '../../data/depth_first_pickle.pkl'
        self.results = self.clear_results()
        self.Folds = self.make_folds()
        
    def make_folds(self):
        # create first state of protein
        amino1 = self.make_amino(self.Protein.protein[0], 0)
        amino2 = self.make_amino(self.Protein.protein[1], 1)
        ancestor = Fold(self.fold_counter, [amino1, amino2], [(0,0), [0,1]], [1])
        children = [ancestor]
        
        # keep going until there are no more children in list
        while children:
            # get last child
            parent = children.pop()
            new_children = self.create_offspring(parent)
            # if new children are created, append to children
            if new_children:
                children.extend(new_children)
            
        # get fold(s) with best scores and turn into Fold object
        final_folds = self.to_fold()
        
        return final_folds
    
    def create_offspring(self, parent):
        # make new children or store final folds
        prev_coords = parent.coordinates
        # if the protein has reached final length, create entry in results
        if len(prev_coords) == self.Protein.bonds:
            self.store_results(parent)
        # else keep creating children
        else:
            # create new children
            new_children = self.make_children(parent)
            return new_children
        
        
    def store_results(self, parent):
        # store each possible child fold in the results
        options = self.check_directions(parent)
        
        for option in options:
            # make new aminoacid
            coordinates = parent.coordinates
            coordinates.append(option)
            new_amino = self.make_amino(type, id)
            new_amino.set_current_coordinate(coordinates[-1])
            new_amino.set_previous_coordinate(coordinates[-2])
            # append info to amino, coord, dir
            aminoacids = parent.aminoacids
            aminoacids.append(new_amino)
            
            # make new result with score
            new_fold = Fold(self.fold_counter, aminoacids, coordinates, directions)
            self.fold_counter += 1
            score = self.Score.calculate_score(new_fold)
            
            # write results to file
            with open(self.filename, 'ab') as file:
                pickle.dump(new_fold, file)
                print(f'Object successfully saved to "{self.filename}"')
    
    def make_children(self, parent):
        
        # MAKE SEPARATE AMINO FOR EACH CHILD
        self.make_amino('H', 'parent_amino_id')
        pass
        
        
    def to_fold(self):
        # find best result(s) and turn into Fold objects
        self.results
            
        
    def make_amino(self, aminotype, parent_amino_id):
        new_amino = Aminoacid(parent_amino_id, aminotype)
        
        return new_amino
    
    
    def check_directions(self, parent):
        coordinates = parent.coordinates
        starting_point = parent.coordinates[-1]
        
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
    
    def clear_results(self):
        # if results file exists, remove
        try:
            os.remove(self.filename)
        except OSError:
            pass