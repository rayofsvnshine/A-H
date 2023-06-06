# from folded_protein import Protein
# from protein_folder import Folder
# from scoring import Score
from sys import argv
import csv

# Load in protein, put in class
# Put protein in Folder
# Output of Folder in Scoring
# Call function for saving score


if __name__ == "__main__":

    # Check command line arguments
    if len(argv) != 2:
        print("Usage: python main.py <protein number>")
        exit(1)

    # Check number of protein
    protein_number = argv[1]

    # Load file
    with open('input/proteins.csv') as csvfile:

            proteins = csv.reader(csvfile, delimiter=',')

            for row in proteins:
                if row[0] == protein_number:
                    protein = row[1]

    print(protein)
