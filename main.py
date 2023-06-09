"""
main.py

* Imports the protein from the proteins.csv file
* Puts protein in Protein class
* Output of Folder in Scoring class
* Exports results to the output.csv file

Pre:
    proteins.csv
Post:
    output.csv
"""

# Import classes and used libraries
from code import Protein
from code import Aminoacid
from code import Score
from code import Fold
from code import Folder

from sys import argv
import csv


def select_protein() -> str:
    """Gives an overview of the available proteins in the csv file."""

    with open("data/proteins.csv", "r") as csvfile:

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

        with open("data/proteins.csv", "r") as csvfile:

            # Read input file
            proteins = csv.reader(csvfile)

            # Select protein
            for row in proteins:
                if row[0] == protein_number:
                    return row[1]
            return False


def export_result(foldingsteps: list, score: int) -> None:
    """Exports results to the output.csv file."""

    with open('data/output.csv', 'w') as csvfile:

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
        selected_protein = import_protein(argv[1])
        if not selected_protein:
            print("Protein not found")
            exit(1)

    # Show proteins from csv file if found
    elif len(argv) == 1:
        if not select_protein():
            print("No proteins found in data/proteins.csv")
            exit(1)
        print(select_protein())

        # Ask user to select a protein
        protein_number = input("Protein number:     ")

        # Import protein if found
        selected_protein = import_protein(protein_number)
        if not selected_protein:
            print("Selected protein not found")
            exit(1)

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

    # Test for Aminoacid object
    print("TEST")
    print(f"First amino_id:     {protein.aminoacids[0].id}")
    print(f"First aminotype:    {protein.aminoacids[0].aminotype}")
    last_aminoacid = len(protein.aminoacids) - 1
    print(f"Last amino_id:      {protein.aminoacids[last_aminoacid].id}")
    print(f"Last aminotype:     {protein.aminoacids[last_aminoacid].aminotype}")
    print("")

    # make random algoritm
    # random_algorithm = Folder(protein)

    # print(len(random_algoritm.Folds))
    # valid_folds = random_algoritm.Folds
    # best_fold = Score.best_score(valid_folds)

    # Test result export
    foldingsteps = [("H", 1), ("H", 2), ("P", -1), ("H", -1), ("P", 2), ("P", 2), ("P", 1), ("P", -2), ("H", 0)]
    score = -2
    export_result(foldingsteps, score)
    print("Results can be found in data/output.csv\n")
