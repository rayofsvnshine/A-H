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
from code.visualisation.visualisation import Visualisation
from code.visualisation.graph import Graph

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


def protein_info_in_terminal(protein: object) -> str:
    """
    Shows information about the protein in the terminal.

    Post:
        Returns a string with information about the protein to print in the main.
    """

    protein.get_totals(protein.protein)
    percentage_h = round(protein.total_h / protein.length * 100)
    percentage_p = round(protein.total_p / protein.length * 100)
    percentage_c = round(protein.total_c / protein.length * 100)

    info = "\n"
    info += "Selected protein:" + " " * 3 + f"{protein.protein}" +"\n"
    info += "Total amino acids:" + " " * 2 + f"{protein.length}" +"\n"

    if protein.total_h > 9:
        info += "Total hydrofobe:" + " " * 4 + f"{protein.total_h}" + " " * 2 + f"{percentage_h}%" + "\n"
    else:
        info += "Total hydrofobe:" + " " * 4 + f"{protein.total_h}" + " " * 3 + f"{percentage_h}%" + "\n"

    if protein.total_p > 9:
        info += "Total polair:" + " " * 7 + f"{protein.total_p}" + " " * 2 + f"{percentage_p}%" + "\n"
    else:
        info += "Total polair:" + " " * 7 + f"{protein.total_p}" + " " * 3 + f"{percentage_p}%" + "\n"

    if protein.total_c > 9:
        info += "Total cysteine:" + " " * 5 + f"{protein.total_c}" + " " * 2 + f"{percentage_c}%"
    else:
        info += "Total cysteine:" + " " * 5 + f"{protein.total_c}" + " " * 3 + f"{percentage_c}%"

    return info


def foldingsteps_in_terminal(foldingsteps: list) -> str:
    """
    Check the foldingsteps in the terminal.

    Pre:
        Foldingsteps is a list of tuples with the amino acid as string.
    Post:
        Returns a string with the foldingsteps to print in the main.
    """

    results = "\n" + "Foldingsteps:" + " " * 7

    for tuple in foldingsteps:
        direction = tuple[1]
        if direction < 0:
            results += "".join(tuple[0]) + " " * 2 + "".join(str(direction)) + "\n" + " " * 20
        else:
            results += "".join(tuple[0]) + " " * 3 + "".join(str(direction)) + "\n" + " " * 20

    return results


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

        # Import protein if found
        selected_protein = import_protein(protein_number)
        if not selected_protein:
            print("Selected protein not found")
            exit(1)

    # Ask user to select an algorithm
    print("\n1    Random algorithm")
    print("2    Monte Carlo simulation")
    print("3    Dijkstra's algorithm\n")
    algorithm_number = input("SELECT ALGORITHM:   ")

    # Run random algoritm
    if algorithm_number == "1":

        # Make new protein object
        print("\nAnalysing protein...")
        protein = Protein(selected_protein)

        # Select number of runs
        print("")
        number_of_runs = input("NUMBER OF RUNS:   ")
        print("")

        # Run algorithm
        print("Running algorithm...")
        random_algorithm = Random(protein, number_of_runs)

        # Calculate score
        print("Calculating score...")
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
        Monte_Carlo = Montecarlo(protein, 10)

        # Calculate score
        print("Calculating score...")
        scorer = Score()
        best_fold = scorer.best_fold(Monte_Carlo.Folds)
        results = best_fold.results 
        score = best_fold.score

        print("Done!")

    # Run ???
    elif algorithm_number == "3":

        # Make new protein object
        print("\nAnalysing protein...")
        protein = Protein(selected_protein)

        # Run algorithm
        print("Running algorithm...")
        # todo

        # Calculate score
        print("Calculating score...")
        # todo

        print("Done!")

    else:
        print("Selected algorithm not found")
        exit(1)

    # Show information about the protein
    print(protein_info_in_terminal(protein))

    # Show score
    if score < 0:
        print("Score:" + " " * 13 + "".join(str(score)) + "\n")
    else:
        print("Score:" + " " * 14 + "".join(str(score)) + "\n")

    # Show foldingsteps in terminal
    show_foldingsteps = input("Show foldingsteps?         [y/n] ")
    if show_foldingsteps == "y":
        print(foldingsteps_in_terminal(results))

    # Create a visualisation of the best fold
    show_visual = input("Show visualisation?        [y/n] ")
    if show_visual == "y":
        visualisation = Visualisation(best_fold)
        visualisation.visualize_protein_plotly_3d()

    # Create a graph of the performnce of the algorithm
    show_graph = input("Show performance graph?    [y/n] ")
    if show_graph == "y":
        graph = Graph(valid_folds)
        graph.algorithm_performance()

    # Export results
    # export_result(results, score)
    print("\nResults can be found in data/output.csv\n")
