from .depth_first import Depth_first
# from ..classes.fold import Fold
from copy import deepcopy
# import pickle

class Pruning(Depth_first):
    """
    Creates a Folder object that can:
    * create folds using a depth-first and pruning algorithm
    """
    
    def __init__(self, Protein: object, pickle_file=False):
        super().__init__(Protein, pickle_file)
        self.prune_values = {}
        
        
    def get_parent(self, parents):
        # get first parent
        first_parent = parents.pop(0)
        new_parents = [first_parent]
        # while first parent in list is of same generation, add to list
        while len(parents[0].aminoacids) == len(first_parent.aminoacids):
            new_parents.append(parents.pop(0))
            
        return new_parents


    def create_offspring(self, parents):
        new_children = []
        for parent in parents:
            # make new children or store final folds
            prev_coords = deepcopy(parent.coordinates)
            # make sure there are options for next aminoacid
            options = self.check_directions(parent)
            if options == None:
                continue
            
            # if the protein has reached final length, create entry in results
            if len(prev_coords) == self.Protein.bonds:
                self.make_children(parent, options, saving=True)
            # else create children to return
            else:
                children = self.make_children(parent, options)
                # prune children
                new_children.append(self.prune_children(children, parent))
        
        if len(new_children) == 0:
            return None
        else:
           return new_children
        
        
    def prune_children(self, new_children, parent):
        # if no children were made, return
        if len(new_children) == 0:
            return None
        # if one child was made, prune
        if len(new_children) < 2:
            
            generation = len(parent.aminoacids)
            
            if self.prune_values[generation]:
                if child.score == self.prune_values[generation]:
                    return [child]
                elif child.score < self.prune_values[generation]:
                    self.prune_values[generation] = child.score
                    return [child]
                else:
                    return None
            else:
                self.prune_values[generation] = child.score
                return [child]
        else:
            if self.prune_values[id]:
                best_score = self.prune_values[id]
            else:
                best_score = 1
            pruned_children = []
            for child in new_children:
                if child.score < best_score:
                    best_score = child.score
                    pruned_children.append(child)
                elif child.score == best_score:
                    pruned_children.append(child)
                else:
                    pass
        
        self.prune_values[id] = best_score
        
        return pruned_children