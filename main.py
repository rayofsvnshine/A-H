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

    with open("input/proteins.csv", "r") as csvfile:

        # Read input file
        proteins = csv.reader(csvfile, delimiter=',')

        # Select protein
        for row in proteins:
            if row[0] == protein_number:
                Protein.protein = row[1]
                return True
        return False


def export_protein(foldingsteps, score):
    """Exports results to the output.csv file."""

    with open('output/output.csv', 'w') as csvfile:

        # Create output file
        output = csv.writer(csvfile)

        # Write column names
        output.writerow(["amino", "fold"])

        # Write folding data
        for step in foldingsteps:
            output.writerow([step[0], step[1]])

        # Write score
        output.writerow(["score", score])

        # OTHER WAY WITH DICTWRITER:

        # # Create two columns
        # output = csv.DictWriter(csvfile, fieldnames = ["amino", "fold"])
        # output.writeheader()

        # # Write folding data
        # for step in foldingsteps:
        #     output.writerow({"amino": step[0], "fold": step[1]})

        # # Write score
        # output.writerow({"amino": "score", "fold": score})


if __name__ == "__main__":

    # Check command line arguments
    if len(argv) != 2:
        print("Usage: python main.py <protein number>")
        exit(1)

    # Import protein if found
    if not import_protein(argv[1]):
        print("Protein not found")
        exit(1)

    # Test protein import
    print(Protein.protein)

    # Test result export
    foldingsteps = [("H", 1), ("H", 2), ("P", -1), ("H", -1), ("P", 2), ("P", 2), ("P", 1), ("P", -2), ("H", 0)]
    score = -2
    export_protein(foldingsteps, score)
