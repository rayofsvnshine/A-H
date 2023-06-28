"""
fold.py

* Stores all properties of the folded protein
"""


class Fold(object):
    """
    Fold object
    """

    def __init__(self, id: int, protein: str, aminoacids: list, coordinates: list):
        """
        Initializer
        """

        self.id = id
        self.protein = protein
        self.aminoacids = aminoacids
        self.coordinates = coordinates
        self.directions = self.calculate_directions()
        self.store_results()

    def calculate_directions(self) -> list:
        """
        Gives the possible directions of an aminoacid.

        """
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

        """
        self.results = []

        for i in range(len(self.aminoacids)):
            self.results.append((self.aminoacids[i].aminotype, self.directions[i]))

    def store_score(self, protein_score: int) -> None:
        """
        Gets the score of a fold to store it in the fold object.

        Parameters:
        ----
        protein_score: an interger that is the calculated score on the folded protein
        """

        self.score = protein_score

    def add_amino(self, aminoacid: object, coordinate: tuple, direction: int):
        """
        Adds the information of a newly appended aminoacid to the existing protein conformation.

        Parameters:
        ----
        aminoacid: object that contains information about one aminoacid
        coordinate: tuple that represents the coordinate one aminoacid is placed on
        direction: interger that represents the direction of the bond the current aminoacid is gonna form with the next
        """
        self.aminoacids.append(aminoacid)
        self.coordinates.append(coordinate)
        self.directions.append(direction)

    def add_to_score(self, score: int):
        """
        Function that adds the score given to the existing score.

        Parameters:
        ----
        score: integer that represents the score of the folded protein
        """
        self.score += score

    def foldingsteps_in_terminal(self) -> str:
        """
        Makes a list of the foldingsteps of a folded protein, which can be shown in the terminal.
        """

        results = "\n" + "Foldingsteps:" + " " * 7

        for tuple in self.results:
            direction = tuple[1]
            if direction < 0:
                results += (
                    "".join(tuple[0])
                    + " " * 2
                    + "".join(str(direction))
                    + "\n"
                    + " " * 20
                )
            else:
                results += (
                    "".join(tuple[0])
                    + " " * 3
                    + "".join(str(direction))
                    + "\n"
                    + " " * 20
                )

        return results
