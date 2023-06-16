""" 
elongation.py
* Class used to store information about elongation used in the Monte Carlo simulation
"""

class Elongation(object):
    """
    Class that is responsible for storing the length, directions and coordinates of the aminoacid sequence
    made in the Monte Carlo simulation. 
    """

    def __init__(self, coordinates:list, directions:list, length_elongation:int):
        """Initializer"""
        self.coordinates = coordinates
        self.directions = directions 
        self.length = length_elongation 


    
    def store_score(self, score):
        """Function that stores the score of the elongation."""
        self.score = score 