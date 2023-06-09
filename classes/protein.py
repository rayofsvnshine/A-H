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

class Protein(object):
    """Protein object"""

    def __init__(self, protein: str):
        """Initializer"""

        self.protein = protein
        self.length = len(self.protein)
        self.bonds = self.length - 1
        self.aminoacids = load_aminoacids()


    def load_aminoacids(self):
        """ Makes list of the aminoacids objects."""
         


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
