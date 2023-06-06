"""
* Imports the protein from the proteins.csv file
* Puts protein in Protein class
* Output of Folder in Scoring class
* Exports results to the output.csv file
"""

# Import classes and used libraries
from classes.folded_protein import Fold
from classes.properties import Protein
from classes.protein_folder import Folder
from classes.scoring import Score
from sys import argv
import csv

def import_protein(protein_number: int) -> bool:
    """Loads the selected protein into the protein class."""

    # Load file
    with open('input/proteins.csv') as csvfile:

        # Read file
        proteins = csv.reader(csvfile, delimiter=',')

        # Select protein
        for row in proteins:
            if row[0] == protein_number:
                Protein.protein = row[1]
                return True
        return False


def export_protein():
    """Exports results to the output.csv file."""
    pass


if __name__ == "__main__":

    # Check command line arguments
    if len(argv) != 2:
        print("Usage: python main.py <protein number>")
        exit(1)

    # Import protein if found
    if not import_protein(argv[1]):
        print("Protein not found")
        exit(1)

    # Print protein (just for checking)
    print(Protein.protein)
