""" 
monte_carlo.py 

* folds a protein in a monte carlo simulation 
* uses the score of the randomly created aminoacid sequence to determine how to extend the protein 
"""

from ..classes.fold import Fold
from ..classes.aminoacid import Aminoacid 
from ..classes.score import Score 
import random
from algorithms.elongation import Elongation

def __init__(self, Protein, n):
    """Initializer"""
    self.protein = Protein.protein
    self.protein_length = Protein.length
    self.starting_point = (0,0)
    self.conformation_coordinates = []
    self.conformation_directions = []
    self.conformation_aminoacids = []
    self.n = n
    self.Folds = make_folds(self.n)
    

def make_folds(self, n):
    """Function that runs the algorithm by calling all the other functions."""
    valid_folds = []
    
    while valid_folds < 5: # loop for number of folds 
        fold_id = 0
        random_length_elongations = random.randint(0, self.protein_length)
        for i in range(self.protein_length): # loop for making the elongations (max is the length of the protein) 
            # make different folded elongations of the same length
            self.make_random_elongations(random_length_elongations, n)
            # select the elongation with the lowest (best) score & checks if elongation can be added to existing conformation
            best_elongation = self.select_elongation(self.elongations)
            # add the best elongation to the existing conformation
            self.adding_elongation(best_elongation)
            # generate a new length for the next random folded elongations 
            random_length_elongations = random.randint(0, (self.protein_length - random_length_elongations))
            # check if the length of the protein is reached, if so, end loop and save the Fold 
            if random_length_elongations == 0:
                break
        # make a new object for the complete fold
        new_fold = Fold(fold_id, self.amino_list, self.conformation_coordinates, self.conformation_directions)
        # increase the fold_id for the next fold
        fold_id += 1 
        # add the new fold to the list of all the valid folds
        valid_folds.append(new_fold)
    
    return valid_folds


def make_random_elongations(self, length_elongation, n):
    """Function makes a random elongation of aminoacids with different lengths."""
    for i in range(n): # loop for the amount of elongation per time want to be made (and checked for the best score)
        self.elongations = []
        coordinates = []
        directions = []
        amino_list = []
        amino_counter = 0
        previous_coordinate = None 

        # make different elongations of the same length in different folds  
        for aminoacid in self.protein:
            ind = 0
            options = self.check_directions(starting_point, coordinates)
            if options == []:
                return None 

            # make new aminoacid 
            new_amino = Aminoacid(self.amino_counter, aminoacid)
            amino_list.append(new_amino)
            self.amino_counter += 1

            # store aminoacid's current position in coordinate list and object
            coordinates.append(starting_point)
            new_amino.store_coordinates(starting_point)
            # set aminoacid's previous coordinate
            new_amino.set_previous_coordinate(previous_coordinate)
            # decide direction and next point of aminoacid chain
            starting_point, direction = self.choose_direction(starting_point, options)
            # save next direction in aminoacid
            new_amino.set_next_direction(starting_point)

            # store direction and change previous coordinate to current coordinate
            directions.append(direction)
            previous_coordinate = starting_point

            # set aminocounter for the next id
            amino_counter += 1 

            # check if length of elongation is reached 
            if ind == length_elongation:
                # make an object of the newly made elongation storing coordinates, directions and the length
                new_elongation = Elongation(coordinates, directions, length_elongation, amino_list)
                # save the elongation in the list of possible elongations 
                self.elongations.append(new_elongation)
                break
    

def check_directions(self, starting_point, coordinates) -> list:
        """
        Determines the coordinate where the following aminoacid will be placed.
        
        Parameters:
        -----
        starting_point = previous coordinate
        coordinates = previous route
        
        Returns:
        -----
        options = list with possible coordinates
        """
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
            
        return next_point, direction

def select_elongation(self):
    """Function gets a random elongation and checks what the score is, after an n number of optimization of the
    elongation, the function returns the sequence with the highest score."""
    max_score = 0
    best_elongation = None 
    for elongation in self.elongations:
        score = elongation.calculate_score_monte_carlo()
        elongation.store_score(score)

        if elongation.score > max_score:
            if self.addition_possible():
                max_score = elongation.score 
                best_elongation = elongation 

    return best_elongation       


def adding_elongation(self, best_elongation):
    """Function gets the aminoacid sequence with the highest score and adds this to the existing protein conformation"""
    self.conformation_coordinates =best_elongation.coordinates
    self.conformation_directions = best_elongation.directions
    self.conformation_aminoacids = best_elongation.

def addition_possible(self):
    """Function checks whether the selected aminoacid sequence can be added to the existing protein conformation."""
    for coordinate in self.elongation.coordinates:
        if coordinate in self.conformation_coordinates:
            return False 
        else:
            return True 

def set_beginning_coordinate(self, last_coordinate):
    """Function stores the new starting coordinate for the rest of the elongation after the last aminoacid sequence is correctly added."""
    self.starting_point == last_coordinate
     