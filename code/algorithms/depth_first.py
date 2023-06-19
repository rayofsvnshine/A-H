"""
depth_first.py

runs a depth first algorithm to find optimal protein folds
"""

from ..classes.fold import Fold
from ..classes.aminoacid import Aminoacid

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
        self.Folds = self.make_folds()
        self.results = {}
        
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
            new_children = self.create_children(parent)
            # if new children are created, append to children
            if new_children:
                children.extend(new_children)
            
        # get fold(s) with best scores and turn into Fold object
        final_folds = self.to_fold()
        
        return final_folds
    
    def create_children(self, parent):
        # make new children or store final folds
        prev_coords = parent.coordinates
        # if the protein has reached final length, create entry in results
        if len(prev_coords) == self.Protein.bonds:
            pass
        # else keep creating children
        else:
            # MAKE SEPARATE AMINO FOR EACH CHILD
            self.make_amino('H', 'parent_amino_id')
            pass
        
        
    def to_fold(self):
        # find best result(s) and turn into Fold objects
        self.results
            
        
    def make_amino(self, aminotype, parent_amino_id):
        new_amino = Aminoacid(parent_amino_id, aminotype)
        
        return new_amino