from classes import Protein, Folder, Score
from sys import argv
import csv

# Load in protein, put in class
# Put protein in Folder
# Output of Folder in Scoring
# Call function for saving score

def import_protein(protein_number: int) -> None:
    """Loads the selected protein into the protein class."""

    # Load file
    with open('input/proteins.csv') as csvfile:

        # Read file
        proteins = csv.reader(csvfile, delimiter=',')

        # Select protein
        for row in proteins:
            if row[0] == protein_number:
                selected_protein = row[1]

        # Store protein
        Protein.protein = selected_protein


if __name__ == "__main__":

    # Check command line arguments
    if len(argv) != 2:
        print("Usage: python main.py <protein number>")
        exit(1)

    # Import selected protein
    import_protein(argv[1])
