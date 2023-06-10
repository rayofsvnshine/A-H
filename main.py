"""
main.py

* Imports the protein from the proteins.csv file
* Puts protein in Protein class
* Runs algorithm
* Output of folded protein in Score class
* Exports results to the output.csv file
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
    """
    Gives an overview of the available proteins.

    Pre:
        The data directory contains a csv file called proteins.
    Post:
        Returns a string showing an overview of all proteins
        that can be found in the data/proteins.csv file. If
        there are no proteins in the file, False is returned.
    """

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
        
        # Returns an overview of all available proteins
        return overview


def import_protein(protein_number: int):
    """
    Loads the selected protein into the protein class.
    
    Pre:
        The protein_number is a integer representing the
        selected protein from the data/proteins.csv file.
    Post:
        Returns the selected protein in a string or returns
        false if the protein is not found.
    """

    with open("data/proteins.csv", "r") as csvfile:

        # Read input file
        proteins = csv.reader(csvfile)

        # Select protein
        for row in proteins:
            if row[0] == protein_number:
                return row[1]
        
        # Returns false if protein is not found
        return False


def export_result(foldingsteps: list, score: int) -> None:
    """
    Exports results to the output.csv file.
    
    Pre:
        Foldingsteps is a list of tuples with the amino acid as
        string and the step as integer and score is an integer.
    Post:
        Writes the results in the data/output.csv file.
    """

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
    last_aminoacid = len(protein.aminoacids) - 1
    print(f"First amino_id:     {protein.aminoacids[0].id}")
    print(f"Last amino_id:      {protein.aminoacids[last_aminoacid].id}")
    print(f"First aminotype:    {protein.aminoacids[0].aminotype}")
    print(f"Last aminotype:     {protein.aminoacids[last_aminoacid].aminotype}")
    print("")

    # make random algoritm
    random_algorithm = Folder(protein)
   
    valid_folds = random_algorithm.Folds
    best_fold = Score.best_fold(valid_folds)
    results = best_fold.results
    score = best_fold.score

    # Test result export
    # results = [("H", 1), ("H", 2), ("P", -1), ("H", -1), ("P", 2), ("P", 2), ("P", 1), ("P", -2), ("H", 0)]
    # score = -2
    export_result(results, score)
    print("Results can be found in data/output.csv\n")
