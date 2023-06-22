""" 
elongation.py

Vera Spek
"""

class Elongation(object):
    """
    Class that is responsible for storing the length, directions and coordinates of the aminoacid sequence
    made in the Monte Carlo simulation. 
    """

    def __init__(self, coordinates:list, directions:list, length_elongation:int, aminoacids, id:int):
        """Initializer"""
        self.id = id
        self.coordinates = coordinates
        self.directions = directions 
        self.length = length_elongation 
        self.aminoacids = aminoacids 


    
    def store_score(self, score):
        """Function that stores the score of the elongation."""
        self.score = score 