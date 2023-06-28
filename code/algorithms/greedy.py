"""
greedy.py
Ray Pelupessy

Object class that runs a Greedy algorithm to fold proteins.
It uses Depth_first as a superclass, but runs as a Breadth first algorithm with pruning.
The pruning function eliminates all options with a less than optimal score.
There is a 5% chance of accepting a less than optimal score to ensure a solution is found.
"""

# import from own code
from .depth_first import Depth_first
# standard imports
from copy import deepcopy
from random import random
import pickle
import operator


class Greedy(Depth_first):
    """
    Creates a Folder object that can:
    * create folds using a breadth-first pruning algorithm
    * iterates over all possible next steps to create child folds
    * prunes child folds by only selecting the folds with the best score
    * has a 5% chance of accepting less than optimal folds (to ensure a solution is found)
    * keeps creating new generations of child folds until the Protein is fully folded
    """
    
    def __init__(self, Protein: object, number_of_runs=1, pickle_file=False):
        """
        Initializes a Depth_first object with Greedy features
        """
        # adds init parameters to super init
        super().__init__(Protein, pickle_file, number_of_runs)
        
        
    def get_parent(self, parents: list):
        """
        Parameters:
        ----
        parents = list of all child folds previously created
        
        Output:
        ----
        parents = list to later put the next parent folds in
        new_parents = all parent folds to be used to create the next generation
        """
        new_parents = deepcopy(parents)
        parents = []
        
        return parents, new_parents


    def create_offspring(self, parents: list):
        """
        Creates next generation of child folds from parent folds
        
        Parameters:
        ----
        parents = list of previous generation folds to create next generation of child folds
        
        Output:
        ----
        None = if there is no next generation OR if results were created and saved
        next_generation = list of child folds
        """
        next_generation = []
        best_score = 1
        
        # loop over all parents in previous generation
        for parent in parents:
            # make sure there are options for next aminoacid
            options = self.check_directions(parent)
            if options == None:
                continue
            
            # create next generation and prune
            new_children = self.make_children(parent, options)
            next_generation, best_score = self.prune_children(best_score, new_children, next_generation)

        # if there is no next generation, return
        if not next_generation:
            return None
        # if the next generation is the full fold, save and return
        elif len(next_generation[0].aminoacids) == len(self.Protein.protein):
            for child in next_generation:
                with open(self.filename, 'ab') as file:
                    pickle.dump(child, file)
            return None
        # if a next generation was created, return
        else:
            return next_generation
        

    def prune_children(self, best_score, new_children, next_generation):
        """
        
        """
        # check every child
        for child in new_children:
            # if the child score is the same as the best score, store child
            if child.score == best_score:
                next_generation.append(child)
            # if the child score is lower than the best score, reset next generation and reassign best score
            elif child.score < best_score:
                next_generation = [child]
                best_score = child.score
            elif random() > 0.95:
                next_generation.append(child)
        # return the next generation and best score
        return next_generation, best_score


    def retrieve_pickle(self, pickle_file):
        """
        
        """
        children = []
        generation = 0
        gen_flag = True
        with open(pickle_file, 'rb') as file:
            while True:
                try:
                    fold = pickle.load(file)
                    for i in range(len(fold)):
                        fold_gen = len(fold[i].aminoacids)
                        if fold_gen != generation:
                            gen_flag = operator.not_(gen_flag)
                            if gen_flag == True:
                                print("\nThe folds are not equally long.")
                                print("Please make sure your previous run is a Pruning run")
                                exit(4)
                    children.append(fold)
                except EOFError:
                    break
                
        return children