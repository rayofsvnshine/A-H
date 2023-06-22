"""
main.py

* Imports the protein from the proteins.csv file
* Puts protein in Protein class
* Runs algorithm
* Output of folded protein in Score class
* Exports results to the output.csv file
"""

from code.classes.protein import Protein
from code.classes.score import Score
from code.algorithms.random import Random
from code.algorithms.montecarlo import Montecarlo
from code.algorithms.depth_first import Depth_first
from code.visualisation.visualisation import Visualisation
from code.visualisation.graph import Graph

from sys import argv
from random import choice
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
        print("Usage: python main.py [protein number]")
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
        protein_number = input("SELECT PROTEIN:     ")

        # Quit if needed
        if protein_number == "q":
            print("\nBye!\n")
            exit(1)

        # Import protein if found
        selected_protein = import_protein(protein_number)
        if not selected_protein:
            print("Selected protein not found")
            exit(1)

    # Ask user to select an algorithm
    print("\n1   Random algorithm")
    print("2   Monte Carlo simulation")
    print("3   Depth first algorithm\n")
    algorithm_number = input("SELECT ALGORITHM:   ")

    # Quit if needed
    if algorithm_number == "q":
        print("\nBye!\n")
        exit(1)

    # Run random algoritm
    if algorithm_number == "1":

        # Select number of runs
        number_of_runs = input("\nNUMBER OF RUNS:     ")

        # Quit if needed
        if number_of_runs == "q":
            print("\nBye!\n")
            exit(1)

        # Make new protein object
        print("\nAnalysing protein...", end =" ")
        protein = Protein(selected_protein)
        print("Done!")

        # Run algorithm
        print("Running algorithm...", end =" ")
        random_algorithm = Random(protein, int(number_of_runs))
        print("Done!")

        # Calculate score
        print("Calculating score...", end =" ")
        valid_folds = random_algorithm.Folds
        scorer = Score()
        best_fold = scorer.best_fold(valid_folds)
        results = best_fold.results
        score = best_fold.score
        print("Done!")

    # Run Monte Carlo Simulation 
    elif algorithm_number == "2":

        # Make new protein object
        print("\nAnalysing protein...")
        protein = Protein(selected_protein)

        # Run algorithm
        print("Running Monte Carlo simulation")
        Monte_Carlo = Montecarlo(protein, 2)

        # Calculate score
        print("Calculating score...")
        scorer = Score()
        best_fold = scorer.best_fold(Monte_Carlo.Folds)
        results = best_fold.results 
        score = best_fold.score

        print("Done!")

    # Run depth first algoritm
    elif algorithm_number == "3":

        # Make new protein object
        print("\nAnalysing protein...")
        protein = Protein(selected_protein)

        # Run algorithm
        print("Running algorithm...")
        depth_first = Depth_first(protein)

        # Calculate score
        print("Calculating score...")
        best_fold = depth_first.Best_fold[0]
        results = best_fold.results
        score = best_fold.score

        print("Done!")

    else:
        print("Selected algorithm not found")
        exit(1)

    # Show information about the protein
    print(protein.protein_info_in_terminal())

    # Show score
    if score < 0:
        print("Score:" + " " * 13 + "".join(str(score)) + "\n")
    else:
        print("Score:" + " " * 14 + "".join(str(score)) + "\n")

    # Show foldingsteps in terminal
    show_foldingsteps = input("Show foldingsteps of best folded protein?   [y/n] ")
    if show_foldingsteps == "q":
        print("\nBye!\n")
        exit(1)
    if show_foldingsteps == "y":
        print(best_fold.foldingsteps_in_terminal())

    # Create a visualisation of the best fold
    show_visual = input("Show visualisation of best folded protein?  [y/n] ")
    if show_visual == "q":
        print("\nBye!\n")
        exit(1)
    if show_visual == "y":
        visualisation = Visualisation(best_fold)
        visualisation.visualize_protein_plotly_3d()

    # Create a graph of the performnce of the algorithm
    show_graph = input("Show algorithm performance graph?           [y/n] ")
    if show_graph == "q":
        print("\nBye!\n")
        exit(1)
    if show_graph == "y":
        graph = Graph(valid_folds)
        graph.algorithm_performance()

    # Export results
    export_result(results, score)
    print("\nResults can be found in data/output.csv\n")
