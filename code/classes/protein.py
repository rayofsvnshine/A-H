"""
protein.py

* Stores length of the protein.
* Stores total amount of bindings.
* Stores total amount of polar aminoacids (P).
* Stores total amount of hydrophobic aminoacids (H).
* Stores total amount of Cysteines.
"""

from .aminoacid import Aminoacid
import csv

class Protein(object):
    """Protein object"""

    def __init__(self, protein: str):
        """
        Initializer
        """

        self.protein = protein
        self.length = len(self.protein)
        self.bonds = self.length - 1
        self.aminoacids = self.load_aminoacids()
        self.total_h = 0
        self.total_p = 0
        self.total_c = 0


    def load_aminoacids(self):
        """
        Makes a list of aminoacid objects.

        Post:
            Loads all amino acids into aminoacids objects and returns them as a list.
        """

        # Create an empty list
        aminoacids = []

        # Start with the first aminoacid in the protein string
        amino_id = 1

        # Loop over all aminoacids the protein string
        for aminoacid in self.protein:

            # Create a new aminoacid object using the aminoacids from the protein string
            new_aminoacid = Aminoacid(id = amino_id, aminotype = aminoacid)

            # Add the aminoacid to self.aminoacids, mapping id to the aminoacid object
            aminoacids.append(new_aminoacid)

            # Move to the next aminoacid id
            amino_id += 1
        
        return aminoacids


    def get_totals(self, protein: str) -> bool:
        """
        Counts all H, P and C amino acids in the protein.

        Pre:
            Protein is a string containing H, P or C amino acids.
        Post:
            Updates the totals of H, P and C.
        """

        for aminoacid in protein:

            if aminoacid == 'H':
                self.total_h += 1

            elif aminoacid == 'P':
                self.total_p += 1

            elif aminoacid == 'C':
                self.total_c += 1

            else:
                return False
