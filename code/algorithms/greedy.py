from .depth_first import Depth_first
from copy import deepcopy
from random import random
import pickle
import operator


class Greedy(Depth_first):
    """
    Creates a Folder object that can:
    * create folds using a depth-first and pruning algorithm
    """
    
    def __init__(self, Protein: object, number_of_runs=1, pickle_file=False):
        super().__init__(Protein, pickle_file, number_of_runs)
        
        
    def get_parent(self, parents):
        new_parents = deepcopy(parents)
        parents = []
        return parents, new_parents


    def create_offspring(self, parents):        
        next_generation = []
        best_score = 1
        
        for parent in parents:
            # make sure there are options for next aminoacid
            options = self.check_directions(parent)
            if options == None:
                continue
            
            # create next generation and prune
            new_children = self.make_children(parent, options)
            next_generation, best_score = self.prune_children(best_score, new_children, next_generation)

        # save final generation or return
        if not next_generation:
            return None
        elif len(next_generation[0].aminoacids) == len(self.Protein.protein):
            for child in next_generation:
                with open(self.filename, 'ab') as file:
                    pickle.dump(child, file)
            return None
        else:
            return next_generation
        

    def prune_children(self, best_score, new_children, next_generation):
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