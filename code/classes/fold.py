"""
fold.py

* Stores all properties of the folded protein
"""

class Fold(object):
    """
    Fold object
    """

    def __init__(self, id: int, aminoacids: list, coordinates: list):
        """
        Initializer
        """

        self.id = id
        self.aminoacids = aminoacids
        self.coordinates = coordinates
        self.directions = self.calculate_directions()
        self.store_results()
        
    
    def calculate_directions(self):
        # loop over coordinates
        length_coords = range(len(self.coordinates) - 1)
        directions = []
        
        for index in length_coords:
            # get coordinates
            current_x = self.coordinates[index][0]
            current_y = self.coordinates[index][1]
            next_x = self.coordinates[index + 1][0]
            next_y = self.coordinates[index + 1][1]
            
            # if there's a difference in y-coordinate, direction is -2 or 2            
            if current_x == next_x:
                # calculate if movement is in positive or negative direction
                direction = next_y - current_y
                direction = 2 * direction
            # if there's a difference in x-coordinate, direction is -1 or 1
            elif current_y == next_y:
                # calculate if movement is in positive or negative direction
                direction = next_x - current_x
            # save direction to list
            directions.append(direction)
        # append 0 for last direction
        directions.append(0)
            
        return directions


    def store_results(self) -> None:
        """
        Makes list with aminoacids and directions.
        
        Pre:
            ...
        Post:
            ...
        """
        self.results = []

        for i in range(len(self.aminoacids)):
            self.results.append((self.aminoacids[i].aminotype, self.directions[i]))


    def store_score(self, protein_score: int) -> None:
        """
        Gets the score of a fold to store it in the fold object.

        Pre:
            ...
        Post:
            ...
        """

        self.score = protein_score
        
    
    def add_amino(self, aminoacid, coordinate, direction):
        self.aminoacids.append(aminoacid)
        self.coordinates.append(coordinate)
        self.directions.append(direction)
        
        
    def add_to_score(self, score):
        self.score += score
