""" 
monte_carlo.py 

Vera Spek 
 
"""

from ..classes.fold import Fold
from ..classes.aminoacid import Aminoacid 
from ..classes.elongation import Elongation
from ..classes.score import Score
import random

class Montecarlo(object):
    """
    Monte Carlo class 
    * Algorithm that uses the addition of parts of the aminosequence with a random length
    * Alorithm selects how the protein is extended by calculating the score according to non-covalent bound H's
    or non-covalent bound C's that are next to eachother. 
    * Algorithm returns a list of valid folds 
    """


    def __init__(self, Protein, n, number_of_runs):
        """Initializer"""
        self.protein = Protein.protein
        self.protein_length = Protein.length
        self.n = n
        self.number_of_runs = number_of_runs
        self.Folds = self.make_folds(self.n)
        


    def make_folds(self, n):
        """
        Fills the list of valid_folds by generating new folds.
        """
        valid_folds = []
        fold_id = 0
        
        # loop for number of folds
        while len(valid_folds) < self.number_of_runs: 
            total_length = self.protein_length
            self.conformation_coordinates = []
            self.conformation_directions = []
            self.conformation_aminoacids = []
            random_length_elongations = random.randint(1, total_length)
            self.where_in_sequence_counter = 0
            self.starting_point = (0,0)
            self.where_in_sequence = []
            self.where_in_sequence[:0] = self.protein
            self.same_length = False

            # loop for making the elongations (max is the length of the protein) 
            for i in range(self.protein_length):
                self.elongations = [] 
                self.same_length = False
                # make n number of elongations
                self.make_random_elongations(random_length_elongations, n)
                # select the elongation with the lowest (best) score & check if elongation can be added to existing conformation
                best_elongation = self.select_elongation()
                # try to make a new fold if no elongation can be added to the existing aminoacid conformation
                if not best_elongation:
                    break
                # remove the aminoacids used in a elongation from the total protein sequence
                self.remove_used_aminoacids(random_length_elongations)
                # add the best elongation to the existing conformation
                self.adding_elongation(best_elongation)
                # generate the new maximum elongation length 
                total_length = total_length - random_length_elongations
                # check if the length of the protein is reached, if so, end loop and save the Fold 
                if total_length == 0:
                    # make a new object for the complete fold
                    new_fold = Fold(fold_id, self.protein, self.conformation_aminoacids, self.conformation_coordinates)
                    # increase the fold_id for the next fold
                    fold_id += 1 
                    # add the new fold to the list of all the valid folds
                    valid_folds.append(new_fold)
                    break
                # set the beginning coordinate to the last coordinate of the used elongation
                self.set_beginning_coordinate(best_elongation.coordinates[-1])
                # generate new random elongation length
                random_length_elongations = random.randint(1, total_length) 
        
        return valid_folds




    def make_random_elongations(self, length_elongation, n):
        """Function makes a random elongation of aminoacids with different lengths."""
        # set elongation id to one 
        elongation_id = 1

        # loop for the amount of elongation per time want to be made (and checked for the best score)
        while len(self.elongations) < n:
            coordinates = []
            directions = []
            self.amino_list = []
            amino_counter = 0
            previous_coordinate = None 
            elongation_length_counter = 1

            if self.same_length:
                self.starting_point = (0,0)

            # make different elongations of the same length with different directions   
            for aminoacid in self.where_in_sequence:
                options = self.check_directions(self.starting_point, coordinates)
                if options == []:
                    self.same_length = True
                    break
                else:   
                    if self.starting_point != (0,0) and not coordinates:
                       self.starting_point, direction = self.choose_direction(self.starting_point, options)
                       options = self.check_directions(self.starting_point, coordinates)
                       if options == []:
                            self.same_length = True
                            break  
                    # make new aminoacid 
                    new_amino = Aminoacid(amino_counter, aminoacid)
                    self.amino_list.append(new_amino)
                    # store aminoacid's current position in coordinate list and object
                    coordinates.append(self.starting_point)
                    # store the current coordinate in the amino acid object
                    new_amino.set_current_coordinate(self.starting_point)
                    # set aminoacid's previous coordinate
                    new_amino.set_previous_coordinate(previous_coordinate)
                    # decide direction and next point of aminoacid chain
                    self.starting_point, direction = self.choose_direction(self.starting_point, options)
                    # save next direction in aminoacid
                    new_amino.set_next_coordinate(self.starting_point)
                    # store direction and change previous coordinate to current coordinate
                    directions.append(direction)
                    # set the previous coordinate 
                    previous_coordinate = self.starting_point
                    # set aminocounter for the next id
                    amino_counter += 1 
                    # check if length of elongation is reached 
                    if elongation_length_counter == length_elongation:
                        self.length_reached(coordinates,directions,length_elongation, elongation_id)
                        self.same_length = True
                        elongation_id += 1
                        break
                    else:
                        elongation_length_counter += 1
        self.same_length = False     
        


        
    def check_directions(self, starting_point, coordinates) -> list:
            """
            Checks which directions are possible to place the coordinate of the next aminoacid.
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
            """
            Picks a random directions from the three possibilities and returns the next coordinate and the chosen direction.
            """
            next_point = random.choice(options)
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
        """
        Gets a random elongation and checks what the score is, after an n number of optimization of the
        elongation, the function returns the sequence with the highest score.
        """
        max_score = 0
        best_elongation = None 
        for elongation in self.elongations:
            score_obj = Score()
            score_elongation = score_obj.calculate_score_monte_carlo(elongation)
            elongation.store_score(score_elongation)
            

            if elongation.score < max_score:
                if self.addition_possible(elongation):
                    max_score = elongation.score 
                    best_elongation = elongation 
        
        if max_score == 0:
            if self.random_addition():
                best_elongation = self.can_append[0]
            else:
                return None 

        return best_elongation       




    def adding_elongation(self, best_elongation):
        """
        Gets the aminoacid sequence with the highest score and adds this to the existing protein conformation
        """
        self.conformation_coordinates.extend(best_elongation.coordinates)
        self.conformation_directions.extend(best_elongation.directions)
        self.conformation_aminoacids.extend(best_elongation.aminoacids)




    def addition_possible(self, elongation):
        """
        Checks whether the selected aminoacid sequence can be added to the existing protein conformation.
        """
        for coordinate in elongation.coordinates:
            if coordinate in self.conformation_coordinates:
                return False 
            else:
                continue
        return True 



    def set_beginning_coordinate(self, last_coordinate):
        """
        Stores the new starting coordinate for the rest of the elongation after the last aminoacid sequence is correctly added.
        """
        self.starting_point = last_coordinate



    
    def length_reached(self, coordinates, directions, length_elongation, id):
        """
        Makes an Elongation object and stores this in the list of all elongations.
        """
        # make an object of the newly made elongation storing coordinates, directions and the length
        new_elongation = Elongation(coordinates, directions, length_elongation, self.amino_list, id)
        # save the elongation in the list of possible elongations 
        self.elongations.append(new_elongation)



    
    def remove_used_aminoacids(self, length_elongation):
        """
        Removes aminoacids that have been used in an elongation from the total protein sequence.
        """
        for i in range(length_elongation):
            # remove the used aminoacid from the aminoacids that can be used
            self.where_in_sequence.pop(0)
    


    def random_addition(self):
        """
        Checks which elongation can be added random to the existing conformation when there is no elongation with a negative score. 
        If no elongation can be added, returns None.
        """
        self.can_append = []
        for elongation in self.elongations:
            if self.addition_possible(elongation):
                self.can_append.append(elongation)
                return True 
        
        if not self.can_append:
            return False
