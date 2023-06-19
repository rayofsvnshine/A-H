"""
depth_first.py

runs a depth first algorithm to find optimal protein folds
"""

from ..classes.fold import Fold
from ..classes.aminoacid import Aminoacid

class Folder(object):
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
        
        def make_folds(self):
            return []