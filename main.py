"""
* Imports the protein from the proteins.csv file
* Puts protein in Protein class
* Output of Folder in Scoring class
* Exports results to the output.csv file
"""

# Import classes and used libraries
# from classes.folded_protein import Fold
from classes.properties import Protein
from classes.protein_folder import Folder
# from classes.scoring import Score
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
        proteins = csv.reader(csvfile)

        # Select protein
        for row in proteins:
            if row[0] == protein_number:
                return row[1]
        return False


def export_protein(foldingsteps: list, score: int) -> None:
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
        else:
            selected_protein = import_protein(argv[1])

    # Show proteins from csv file if found
    elif len(argv) == 1:
        if not select_protein():
            print("No proteins found in proteins.csv")
            exit(1)
        print(select_protein())

        # Ask user to select a protein
        protein_number = input("Protein number:     ")

        # Import protein if found
        if not import_protein(protein_number):
            print("Selected protein not found")
            exit(1)
        else:
            selected_protein = import_protein(protein_number)

    # Make new protein object
    protein = Protein(selected_protein)

    # Checkout the selected protein
    print("")
    print(f"Selected protein:   {protein.protein}")
    print(f"Total amino acids:  {protein.length}")
    protein.get_totals(protein.protein)
    print(f"Total hydrofobe:    {protein.total_h}  ({round(protein.total_h / protein.length * 100)}%)")
    print(f"Total polair:       {protein.total_p}  ({round(protein.total_p / protein.length * 100)}%)")
    print(f"Total cysteine:     {protein.total_c}  ({round(protein.total_c / protein.length * 100)}%)")
    print("")

    new_protein_fold = Folder(protein)

    # Test result export
    foldingsteps = [("H", 1), ("H", 2), ("P", -1), ("H", -1), ("P", 2), ("P", 2), ("P", 1), ("P", -2), ("H", 0)]
    score = -2
    export_protein(foldingsteps, score)
    print("Results can be found in output.csv\n")
