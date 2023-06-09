"""
protein.py

* Stores length of the protein.
* Stores total amount of bindings.
* Stores total amount of polar aminoacids (P).
* Stores total amount of hydrophobic aminoacids (H).
* Stores total amount of Cysteines.

Pre:
    Protein chain (str).
Post:
    Initialises the different properties of the protein.
"""
from .aminoacid import Aminoacid

class Protein(object):
    """Protein object"""

    def __init__(self, protein: str):
        """Initializer"""

        self.protein = protein
        self.length = len(self.protein)
        self.bonds = self.length - 1
        self.aminoacids = {}


    def load_aminoacids(self):
        """ Makes list of the aminoacids objects."""

        # Start with the first aminoacid in the protein string
        amino_id = 1

        # Loop over all aminoacids the protein string
        for aminoacid in self.protein:

            # Create a new aminoacid object using the aminoacids from the protein string
            new_aminoacid = Aminoacid(id = amino_id, aminotype = aminoacid)

            # Add the aminoacid to self.aminoacids, mapping id to the aminoacid object
            self.aminoacids.update({new_aminoacid.id: new_aminoacid.aminotype})

            # Move to the next aminoacid id
            amino_id += 1


    def get_totals(self, protein: str) -> bool:
        """ Gets a string containing H, P or C aminoacids and counts their amounts."""

        self.total_h = 0
        self.total_p = 0
        self.total_c = 0

        for element in protein:

            if element == 'H':
                self.total_h += 1

            elif element == 'P':
                self.total_p += 1

            elif element == 'C':
                self.total_c += 1

            else:
                return False
