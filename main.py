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


def select_protein() -> str:
    """Gives an overview of the available proteins in the csv file."""

    with open("proteins.csv", "r") as csvfile:

        # Read input file
        proteins = [row for row in csv.reader(csvfile)]

        # Check if there are proteins in the file
        if len(proteins) == 0:
            return False

        # Create an overview
        overview = "\n"
        for row in proteins:
            overview += "   ".join(row) + "\n"
        return overview


def import_protein(protein_number: int) -> bool:
    """Loads the selected protein into the protein class."""

    with open("proteins.csv", "r") as csvfile:

        # Read input file
        proteins = csv.reader(csvfile, delimiter=',')

        # Select protein
        for row in proteins:
            if row[0] == protein_number:
                Protein.protein = row[1]
                return True
        return False


def export_protein(foldingsteps, score) -> None:
    """Exports results to the output.csv file."""

    with open('output.csv', 'w') as csvfile:

        # Create output file
        output = csv.writer(csvfile)

        # Write column names
        output.writerow(["amino", "fold"])

        # Write folding data
        for step in foldingsteps:
            output.writerow([step[0], step[1]])

        # Write score
        output.writerow(["score", score])


if __name__ == "__main__":

    # Check command line arguments
    if len(argv) >= 3:
        print("Usage: python main.py <protein number>")
        exit(1)

    # Import protein if found
    elif len(argv) == 2:
        if not import_protein(argv[1]):
            print("Protein not found")
            exit(1)

    # Show proteins from csv file if found
    elif len(argv) == 1:
        if not select_protein():
            print("No proteins found in proteins.csv")
            exit(1)
        print(select_protein())

        # Ask user to select a protein
        protein_number = input("Select a protein: ")

        # Import protein if found
        if not import_protein(protein_number):
            print("Selected protein not found")
            exit(1)

    # Check the selected protein
    print(f"Selected protein: {Protein.protein}")

    # Test result export
    foldingsteps = [("H", 1), ("H", 2), ("P", -1), ("H", -1), ("P", 2), ("P", 2), ("P", 1), ("P", -2), ("H", 0)]
    score = -2
    export_protein(foldingsteps, score)
    print("Results can be found in output.csv")
