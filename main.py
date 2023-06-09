"""
main.py
    * Gives an overview of the available proteins.
    * Imports the protein from the proteins.csv file.
    * Puts protein in Protein class.
    * Runs the algorithm that is selected by the user.
    * Gives terminal feedback to the user.
    * Exports all scores for all runs to a scores_<algorithm_name>.csv file.
    * Exports foldingsteps and score to the output.csv file.
"""

from code.classes.protein import Protein
from code.classes.score import Score
from code.algorithms.random import Random
from code.algorithms.FRESS import FRESS
from code.algorithms.depth_first import Depth_first
from code.algorithms.greedy import Greedy
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


def import_protein(protein_number: int) -> bool:
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

    with open("data/output.csv", "w") as csvfile:

        # Create output file
        output = csv.writer(csvfile)

        # Write column names
        output.writerow(["amino", "fold"])

        # Write folding data
        for step in foldingsteps:
            output.writerow([step[0], step[1]])

        # Write score
        output.writerow(["score", score])


def check_quit(user_input: str) -> None:
    """
    Check if the user wants to quit the program.

    Pre:
        The parameter user_input is a string contaning the user input.
    Post:
        Prints bye and exits the program.
    """

    if user_input == "q":
        print("\nBye!\n")
        exit(1)


def create_protein_object(selected_protein: int) -> object:
    """
    Creates a protein object.

    Pre:
        The parameter selected_protein is a integer, representing the protein number.
    Post:
        Returns a protein object.
    """

    print("\nAnalysing protein...", end=" ")
    protein = Protein(selected_protein)
    print("done!")
    return protein


def export_scores(valid_folds: list, algorithm_name: str) -> None:
    """
    Exports the scores to a csv file so it can be accesed later.

    Pre:
        The parameter valid_folds is a list containing valid fold objects.
        The parameter algorithm_name is a string containing the name of the algorithm.
    Post:
        Creates a csv file with the name of the algorithm contaning all scores.
    """

    with open(f"data/scores_{algorithm_name}.csv", "w") as csvfile:

        # Create output file
        output = csv.writer(csvfile)

        # Write score data
        for score in valid_folds:
            output.writerow([score])


def import_scores(algorithm_name: str) -> list:
    """
    Imports the scores from the csv file with valid folding scores.

    Pre:
        The parameter algorithm_name is a string containing the name of the algorithm.
    Post:
        Returns a list with all the valid folding scores.
    """

    with open(f"data/scores_{algorithm_name}.csv", "r") as csvfile:

        # Read input file
        input = csv.reader(csvfile)

        # Load scores
        scores = []
        for row in input:
            scores.append(int(row[0]))

        # Returns the scores
        return scores


if __name__ == "__main__":

    # Check command line arguments
    if len(argv) >= 3:
        print("\nUsage: python main.py [protein number]\n")
        exit(1)

    # Import protein if found
    elif len(argv) == 2:
        selected_protein = import_protein(argv[1])
        if not selected_protein:
            print("\nProtein not found :(\n")
            exit(1)

    # Show proteins from csv file if found
    elif len(argv) == 1:

        # Ask for new run
        answer = input("\nAnalyse a new protein (n) or analyse existing data (e)? ")

        # Quit if needed
        check_quit(answer)

        # Analyse new protein
        if answer == "n":

            if not select_protein():
                print("\nNo proteins found in data/proteins.csv :(\n")
                exit(1)
            print(select_protein())

            # Ask user to select a protein
            protein_number = input("Which protein would you like to use? ")

            # Quit if needed
            check_quit(protein_number)

            # Import protein if found
            selected_protein = import_protein(protein_number)
            if not selected_protein:
                print("\nSelected protein not found :(\n")
                exit(1)

        # Analyse existing data
        if answer == "e":

            # import scores
            scores_random = import_scores("Random")
            scores_FRESS = import_scores("FRESS")
            scores_greedy = import_scores("Greedy")

            # Create graph end exit prompt
            Graph.algorithm_comparison(scores_random, scores_FRESS, scores_greedy)
            exit(1)

    # Ask user to select an algorithm
    print("\n1   Random algorithm")
    print("2   FRESS ")
    print("3   Depth first algorithm")
    print("4   Greedy algorithm\n")
    algorithm_number = input("Which algorithm would you like to use? ")

    # Quit if needed
    check_quit(algorithm_number)

    # Run random algoritm
    if algorithm_number == "1":

        # Select number of runs
        number_of_runs = input("How many times do you want to run the algorithm? ")

        # Quit if needed
        check_quit(number_of_runs)

        # Make new protein object
        protein = create_protein_object(selected_protein)

        # Run algorithm
        print("Running algorithm...", end=" ")
        random_algorithm = Random(protein, int(number_of_runs))
        print("done!")

        # Calculate score
        print("Calculating score...", end=" ")
        valid_folds = random_algorithm.Folds
        scorer = Score()
        best_fold = scorer.best_fold(valid_folds)
        results = best_fold.results
        score = best_fold.score
        print("done!")

        # Export scores for graph
        algorithm_name = "Random"
        scores = []
        for fold in valid_folds:
            scores.append(fold.score)
        export_scores(scores, algorithm_name)

    # Run Monte Carlo Simulation
    elif algorithm_number == "2":

        # Select number of runs
        number_of_runs = input("How many times do you want to run the algorithm? ")

        # Quit if needed
        check_quit(number_of_runs)

        # Select number of times an elongation is going to be folded
        number_of_folds_elongations = input(
            "How many times do you want the elongations to be folded? "
        )
        check_quit(number_of_folds_elongations)

        # Make new protein object
        protein = create_protein_object(selected_protein)

        # Run algorithm
        print("Running algorithm...", end=" ")
        FRESS = FRESS(protein, int(number_of_folds_elongations), int(number_of_runs))
        valid_folds = FRESS.Folds
        print("done!")

        # Calculate score
        print("Calculating score...", end=" ")
        scorer = Score()
        best_fold = scorer.best_fold(valid_folds)
        results = best_fold.results
        score = best_fold.score
        print("done!")

        # Export scores for graph
        algorithm_name = "FRESS"
        scores = []
        for fold in valid_folds:
            scores.append(fold.score)
        export_scores(scores, algorithm_name)

    # Run depth first algoritm
    elif algorithm_number == "3":

        answer = input("Start a new run (n) or continue last run (c)? ")
        check_quit(answer)

        # Make new protein object
        protein = create_protein_object(selected_protein)

        # Run algorithm
        print("Running algorithm...", end=" ")
        if answer == "n":
            depth_first = Depth_first(protein)
        elif answer == "c":
            depth_first = Depth_first(protein, pickle_file=True)
        print("done!")

        # Calculate score
        print("Calculating score...", end=" ")
        best_fold = depth_first.Best_fold[0]
        results = best_fold.results
        score = best_fold.score
        print("done!")

    elif algorithm_number == "4":

        answer = input("Start a new run (n) or continue last run (c)? ")
        check_quit(answer)

        # Run algorithm
        if answer == "n":
            # Select number of runs
            number_of_runs = input("How many times do you want to run the algorithm? ")

            # Quit if needed
            check_quit(number_of_runs)

            # Make new protein object
            protein = create_protein_object(selected_protein)

            print("Running algorithm...", end=" ")
            greedy = Greedy(protein, number_of_runs)

        elif answer == "c":
            print("Running algorithm...", end=" ")
            protein = Protein(selected_protein)
            greedy = Greedy(protein, pickle_file=True)

        if greedy.Best_fold:
            valid_folds = greedy.Best_fold
            print("done!")
        else:
            print("\nNo folds were found :(")
            print("Please restart program and continue running to find a fold")
            exit(1)

        # Calculate score
        print("Calculating score...", end=" ")
        valid_folds = greedy.Best_fold
        scorer = Score()
        best_fold = scorer.best_fold(valid_folds)
        results = best_fold.results
        score = best_fold.score
        print("done!")

        # Export scores for graph
        algorithm_name = "Greedy"
        scores = []
        for fold in valid_folds:
            scores.append(fold.score)
        export_scores(scores, algorithm_name)

    else:
        print("\nSelected algorithm not found :(\n")
        exit(1)

    # Show information about the protein
    print(protein.protein_info_in_terminal())

    # Show score
    if score < 0:
        print("Score:" + " " * 13 + "".join(str(score)) + "\n")
    else:
        print("Score:" + " " * 14 + "".join(str(score)) + "\n")

    # Create a visualisation of the best fold
    show_visual = input("Show visualisation of the best folded protein? [y/n] ")
    check_quit(show_visual)
    if show_visual == "y":
        visualisation = Visualisation(best_fold)
        visualisation.visualize_protein_plotly_3d()

    # Show foldingsteps in terminal
    show_foldingsteps = input("Show foldingsteps of the best folded protein?  [y/n] ")
    check_quit(show_foldingsteps)
    if show_foldingsteps == "y":
        print(best_fold.foldingsteps_in_terminal())

    # Create a graph of the performnce of the random algorithm
    if algorithm_number != "3":
        show_graph = input("Show the algorithm performance graph?          [y/n] ")
        check_quit(show_graph)
        if show_graph == "y":
            graph = Graph(valid_folds)
            graph.algorithm_performance(algorithm_name)

    # Export results
    export_result(results, score)
    print("\nResults can be found in data/output.csv\n")
