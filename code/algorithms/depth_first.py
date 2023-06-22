"""
depth_first.py

runs a depth first algorithm to find optimal protein folds
"""

from ..classes.fold import Fold
from ..classes.aminoacid import Aminoacid
from ..classes.score import Score
import pickle
import copy
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
        self.fold_counter = 0
        self.Score = Score()
        self.filename = 'data/depth_first_pickle.pkl'
        self.clear_results()
        self.make_folds()
        self.Best_fold = self.determine_best_fold()
        self.clear_results()
        
    def make_folds(self):
        # create first state of protein
        ancestor = self.create_ancestor()
        children = [ancestor]
        
        # keep going until there are no more children in list
        while children:
            # get last child
            parent = children.pop()
            new_children = self.create_offspring(parent)
            # if new children are created, append to children
            if new_children:
                children.extend(new_children)
        
    
    def create_offspring(self, parent):
        # make new children or store final folds
        prev_coords = copy.deepcopy(parent.coordinates)
        # make sure there are options for next aminoacid
        options = self.check_directions(parent)
        if options == None:
            return None
        
        # if the protein has reached final length, create entry in results
        if len(prev_coords) == self.Protein.bonds:
            self.make_children(parent, options, saving=True)
            return None
        # else create children to append
        else:
            new_children = self.make_children(parent, options)
            return new_children

    
    def make_children(self, parent, options, saving=False):
        # get all possible directions
        children = []
        
        # make all possible children of parent
        for option in options:
            # store coordinates
            coordinates = copy.deepcopy(parent.coordinates)
            coordinates.append(option)
            # make new aminoacid
            new_amino = self.make_amino(parent, option)
            # append to amino list
            aminoacids = copy.deepcopy(parent.aminoacids)
            aminoacids.append(new_amino)
            
            # make complete Fold with score
            new_fold = Fold(self.fold_counter, aminoacids, coordinates)
            self.fold_counter += 1
            score = self.Score.calculate_score(new_fold)
            new_fold.store_score(score)
            children.append(new_fold)
            
            # if final fold, save to file
            if saving == True:
                with open(self.filename, 'ab') as file:
                    pickle.dump(new_fold, file)
        
        if saving == False:
            return children

        
    def make_amino(self, parent, coordinate):
        # makes aminoacid object
        # get parent id and aminotype of child amino
        parent_amino = parent.aminoacids[-1]
        parent_amino_id = parent_amino.id
        own_id = parent_amino_id + 1
        # print(self.Protein.protein, own_id)
        aminotype = self.Protein.protein[own_id]
        
        new_amino = Aminoacid(own_id, aminotype)
        new_amino.set_previous_coordinate(parent.coordinates[-1])
        new_amino.set_current_coordinate(coordinate)
        
        return new_amino
    
    
    def check_directions(self, parent):
        # goes over all possible options to put next aminoacid
        coordinates = copy.deepcopy(parent.coordinates)
        starting_point = coordinates[-1]
        
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
        
    
    def determine_best_fold(self):
        # read results file and return best folds
        best_score = 1
        best_fold = []
        
        with open(self.filename, 'rb') as file:
            while True:
                try:
                    fold = pickle.load(file)
                    if fold.score < best_score:
                        best_fold = [fold]
                        best_score = fold.score
                    elif fold.score == best_score:
                        best_fold.append(fold)
                    else:
                        continue
                except EOFError:
                    break
                
        return best_fold
    
    def create_ancestor(self):
        # creates initial fold from which all other child folds are created
        coordinate1 = (0,0)
        coordinate2 = (0,1)
        amino1 = Aminoacid(0, self.Protein.protein[0])
        amino1.set_current_coordinate(coordinate1)
        amino1.set_next_coordinate(coordinate2)
        amino2 = Aminoacid(1, self.Protein.protein[1])
        amino2.set_previous_coordinate(coordinate1)
        amino2.set_current_coordinate(coordinate2)
        
        ancestor = Fold(self.fold_counter, [amino1, amino2], [coordinate1, coordinate2])
        return ancestor