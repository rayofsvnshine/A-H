"""
protein.py

* Stores length of the protein.
* Stores total amount of bindings.
* Stores total amount of polar aminoacids (P).
* Stores total amount of hydrophobic aminoacids (H).
* Stores total amount of Cysteines (C).
* Calculates and stores the theoretical lower bound.
"""

from .aminoacid import Aminoacid


class Protein(object):
    """
    Protein object
    """

    def __init__(self, protein: str):
        """
        Initializes the protein class.

        Parameters:
        ----
        protein: a string of the sequence of the aminoacid types of a protein.
        """

        self.protein = protein
        self.length = len(self.protein)
        self.bonds = self.length - 1
        self.aminoacids = self.load_aminoacids()
        self.total_h = 0
        self.total_p = 0
        self.total_c = 0
        self.get_totals()
        self.lower_bound = self.theoretical_lower_bound()

    def load_aminoacids(self):
        """
        Makes a list of aminoacid objects.

        """

        # Create an empty list
        aminoacids = []

        # Start with the first aminoacid in the protein string
        amino_id = 1

        # Loop over all aminoacids the protein string
        for aminoacid in self.protein:
            # Create a new aminoacid object using the aminoacids from the protein string
            new_aminoacid = Aminoacid(id=amino_id, aminotype=aminoacid)

            # Add the aminoacid to self.aminoacids, mapping id to the aminoacid object
            aminoacids.append(new_aminoacid)

            # Move to the next amino acid id
            amino_id += 1

        # Return the list of amino acids
        return aminoacids

    def get_totals(self) -> None:
        """
        Counts all H, P and C amino acids in the protein.

        """

        # Loop over all aminoacids in the protein string
        for aminoacid in self.protein:
            # Count the H, P and C amino acids in the string
            if aminoacid == "H":
                self.total_h += 1
            elif aminoacid == "P":
                self.total_p += 1
            elif aminoacid == "C":
                self.total_c += 1

    def protein_info_in_terminal(self) -> str:
        """
        Makes a list of percentage per aminotype, total amount of aminoacids and the amount of hydrophobic, polair and C aminoacids,
        which can be shown in the terminal.
        """

        # Calculate the percentage for H, P and C
        percentage_h = round(self.total_h / self.length * 100)
        percentage_p = round(self.total_p / self.length * 100)
        percentage_c = round(self.total_c / self.length * 100)

        # Create a string with the protein information
        info = "\n"
        info += "Selected protein:" + " " * 3 + f"{self.protein}" + "\n"
        info += "Total amino acids:" + " " * 2 + f"{self.length}" + "\n"

        # Set correct spacing
        if self.total_h > 9:
            info += (
                "Total hydrofobe:"
                + " " * 4
                + f"{self.total_h}"
                + " " * 2
                + f"{percentage_h}%"
                + "\n"
            )
        else:
            info += (
                "Total hydrofobe:"
                + " " * 4
                + f"{self.total_h}"
                + " " * 3
                + f"{percentage_h}%"
                + "\n"
            )

        # Set correct spacing
        if self.total_p > 9:
            info += (
                "Total polair:"
                + " " * 7
                + f"{self.total_p}"
                + " " * 2
                + f"{percentage_p}%"
                + "\n"
            )
        else:
            info += (
                "Total polair:"
                + " " * 7
                + f"{self.total_p}"
                + " " * 3
                + f"{percentage_p}%"
                + "\n"
            )

        # Set correct spacing
        if self.total_c > 9:
            info += (
                "Total cysteine:"
                + " " * 5
                + f"{self.total_c}"
                + " " * 2
                + f"{percentage_c}%"
                + "\n"
            )
        else:
            info += (
                "Total cysteine:"
                + " " * 5
                + f"{self.total_c}"
                + " " * 3
                + f"{percentage_c}%"
                + "\n"
            )

        # Set correct spacing
        if self.lower_bound < 0:
            info += "Theoretical LB:" + " " * 4 + f"{self.lower_bound}"
        else:
            info += "Theoretical LB:" + " " * 5 + f"{self.lower_bound}"

        # Return the string with protein information
        return info

    def theoretical_lower_bound(self) -> int:
        """
        Calculates the theoretical lower bound of the objective function.
        """

        # Create lower bound
        lowerbound = 0

        # Check all C and H amino acids
        lowerbound -= self.total_h * 2 + self.total_c * 10

        # Correct the first amino acid
        if self.protein[0] == "H":
            lowerbound -= 1
        elif self.protein[0] == "C":
            lowerbound -= 5

        # Correct the last amino acid
        if self.protein[len(self.protein) - 1] == "H":
            lowerbound -= 1
        elif self.protein[len(self.protein) - 1] == "C":
            lowerbound -= 5

        # Only half of the bonds can connect so divided by 2 times 2
        lowerbound = round(lowerbound / 2)

        # Return result
        return lowerbound
