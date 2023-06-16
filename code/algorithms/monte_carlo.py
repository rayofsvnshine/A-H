""" 
monte_carlo.py 

* folds a protein in a monte carlo simulation 
* uses the score of the randomly created aminoacid sequence to determine how to extend the protein 
"""

from ..classes.fold import Fold
from ..classes.aminoacid import Aminoacid 
from ..classes.score import Score 
import random
from elongation.py import elongation

def __init__(self, Protein):
    """Initializer"""
    self.protein = Protein.protein
    self.protein_length = Protein.length
    self.Folds = make_folds()

def make_folds():
    """Function that runs the algorithm by calling all the other functions."""
    valid_folds = []
    possible_length_elongation = random.randint(0, self.protein_length)
    
    new_elongation = None 

    while valid_folds < 5: 
        for i in range(self.protein_length):  #This range can be changed to how many folds want to be made
            new_elongation = make_random_elongation(possible_length_elongation)
            select_elongation(new_elongation)
    
        if addition_possible():
            adding_elongation()
            possible_length_elongation = random.randint(0, (self.protein_length - possible_length_elongation))
            if possible_length_elongation == 0:
                break
        
        else:
            break


def make_random_elongation(self,n):
    """Function makes a random elongation of aminoacids with different lengths."""
    self.elongations = []
    starting_point = (0,0)
    coordinates = []
    directions = []
    previous_coordinate = None 
    for aminoacid in self.protein:
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
        
    new_elongation = elongation(coordinates, directions, n)

    self.elongations.append(new_elongation)

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
            max_score = elongation.score 
            best_elongation = elongation        


def adding_elongation(self):
    """Function gets the aminoacid sequence with the highest score and adds this to the existing protein conformation"""
    pass 

def addition_possible(self):
    """Function checks whether the selected aminoacid sequence can be added to the existing protein conformation."""
    pass

def set_beginning_coordinate(self):
    """Function stores the new starting coordinate for the rest of the elongation after the last aminoacid sequence is correctly added."""
    pass 