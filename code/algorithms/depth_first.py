"""
depth_first.py
Ray Pelupessy

Runs a depth first algorithm to find optimal protein folds.
Iterates over all possible options, saves these results to a pickle file.
If a keyboard interrupt occurs, will save all currently created folds to another pickle file.
Can continue running from previously created pickle files.
When done with running, will iterate over the pickle file and determine the best fold found.
"""

# import own code
from ..classes.fold import Fold
from ..classes.aminoacid import Aminoacid
from ..classes.score import Score
# import python libraries
import pickle
import copy
import os

class Depth_first(object):
    """
    Creates an object that can:
    * create folds using a depth-first approach
    * saves all results to a pickle file
    * find the best result in this pickle file and store it
    * if user uses keyboard interrupt the program will store current folds
    * user can continue running program with previously created data
    Results are stored in self.Best_fold
    """

    def __init__(self, Protein: object, pickle_file=False, number_of_runs=1):
        """
        Initializes a Folder object
        
        Parameters:
        ----
        Protein = Protein object that needs to be folded
        pickle_file = filepath of the file where previous data was stored
        number_of_runs = how many times you want to run the code (for depth-first this should
        be left at 1)
        """
        self.Protein = Protein
        self.fold_counter = 0
        self.Score = Score()
        self.filename = 'data/depth_first_pickle.pkl'
        self.Best_fold = []
        self.number_of_runs = range(int(number_of_runs))
        # run code for as many iterations as user indicated
        for run in self.number_of_runs:
            # clears previously generated results if needed
            if not pickle_file or run > 0:
                self.clear_results()
            self.make_folds(pickle_file)
            # if file exists, determine best fold
            if os.path.exists(self.filename):
                solution = self.determine_best_fold()
                self.Best_fold.append(solution)
            # TODO: REMOVE
            else:
                continue

        
    def make_folds(self, pickle_file: str):
        """
        Makes folds from new protein or pickle data and stores them
        
        Parameters:
        ----
        pickle_file = filepath of pickle file with data from a previous run
        """
        # create first state of protein or retrieve parents from pickle file
        if pickle_file:
            children = self.retrieve_pickle('data/pause_run.pkl')[0]
            self.check_protein(children)
        else:
            ancestor = self.create_ancestor()
            children = [ancestor]
        
        # keep going until there are no more children in list
        while children:
            try:
                # get last child
                children, parent = self.get_parent(children)
                new_children = self.create_offspring(parent)
            # if keyboard interrupt -> save children
            except KeyboardInterrupt:
                try:
                    with open('data/pause_run.pkl', 'wb') as file:
                        pickle.dump(children, file)
                        print('\nOh no! You interrupted the program.')
                        print('Best result from currently found folds is being determined.')
                        break
                except KeyboardInterrupt:
                    print('\nWhat!? Why did you do that!?')
                    print('\nThe children were not saved... :(')
                    break
                
            # if new children are created, append to children
            if new_children:
                children.extend(new_children)
                
    
    def get_parent(self, parents: list) -> tuple:
        """
        Returns parent to create next children from
        
        Parameters:
        ----
        parents = list of fold objects
        
        Output:
        ----
        new_parent = the final entry in the parents list
        parents = the parents list without the new_parent
        """
        new_parent = parents.pop()
        return parents, new_parent
        
    
    def create_offspring(self, parent: object):
        """
        Creates the next generation of children from a given parent
        
        Parameters:
        ----
        parent = the parent fold from which the children are created
        
        Output:
        ----
        None = if the final generation is reached, children will be saved to pickle file
        new_children = the new children to be appended to parent list
        """
        # copy coordinate list from parent
        prev_coords = copy.deepcopy(parent.coordinates)
        # make sure there are options for next aminoacid
        options = self.check_directions(parent)
        if options == None:
            return None
        
        # if the protein has reached final length, create entry in results
        if len(prev_coords) == self.Protein.bonds:
            self.make_children(parent, options, saving=True)
            return None
        # else create children to append to parent list
        else:
            new_children = self.make_children(parent, options)
            return new_children

    
    def make_children(self, parent: object, options: list, saving=False) -> list:
        """
        Creates all possible children from parent fold and either save or return them
        
        Parameters:
        ----
        parent = the parent fold from which the child folds are created
        options = list of coordinates the child folds will use
        saving = bool to indicate if this is the final generation
        
        Output:
        ----
        None = if the children were stored in the pickle file
        children = if the children are to be appended to the parent list
        """
        children = []
        
        # make all possible children of parent
        for option in options:
            # store coordinates
            coordinates = copy.deepcopy(parent.coordinates)
            coordinates.append(option)
            # make new aminoacid
            new_amino = self.make_amino(parent, option)
            # append to amino list
            aminoacids = copy.deepcopy(parent.aminoacids)
            aminoacids.append(new_amino)
            
            # make complete Fold with score
            new_fold = Fold(self.fold_counter, self.Protein.protein, aminoacids, coordinates)
            self.fold_counter += 1
            score = self.Score.calculate_score(new_fold)
            new_fold.store_score(score)
            children.append(new_fold)
            
            # if final fold, save to file
            if saving == True:
                with open(self.filename, 'ab') as file:
                    pickle.dump(new_fold, file)
        
        if saving == False:
            return children

        
    def make_amino(self, parent: object, coordinate: tuple) -> object:
        """
        Creates an Aminoacid object and initializes its previous and current coordinate
        
        Parameters:
        ----
        parent = Fold object
        coordinate = tuple of coordinates where the aminoacid is located
        
        Output:
        ----
        new_amino = an Aminoacid object
        """
        # makes aminoacid object
        # get parent id and aminotype of child amino
        parent_amino = parent.aminoacids[-1]
        parent_amino_id = parent_amino.id
        own_id = parent_amino_id + 1
        aminotype = self.Protein.protein[own_id]
        
        new_amino = Aminoacid(own_id, aminotype)
        new_amino.set_previous_coordinate(parent.coordinates[-1])
        new_amino.set_current_coordinate(coordinate)
        
        return new_amino
    
    
    def check_directions(self, parent: object) -> list:
        """
        Checks all surrounding coordinates for possible ways to make the next fold
        
        Parameters:
        ----
        parent = the parent fold with all previous coordinates
        
        Output:
        ----
        options = list of valid coordinates
        """
        # goes over all possible options to put next aminoacid
        coordinates = copy.deepcopy(parent.coordinates)
        starting_point = coordinates[-1]
        
        orientations = [(0,1), (0,-1), (1,0), (-1,0)]
        options = []
        
        # for each direction, check if it has already been visited or not and append if not
        for plus_x, plus_y in orientations:
            x, y = starting_point
            new_x = x + plus_x
            new_y = y + plus_y
            if (new_x, new_y) in coordinates:
                continue
            else:
                options.append(((new_x), (new_y)))
                
        return options
    
    def clear_results(self):
        """
        if the results file exists, remove it
        """
        # if results file exists, remove
        try:
            os.remove(self.filename)
        except OSError:
            pass
        
        
    def retrieve_pickle(self, pickle_file: str) -> list:
        """
        loads in all the fold objects from a previous run, as stored in the pickle file
        
        Parameters:
        ----
        pickle_file = filepath to the pickle file
        
        Output:
        ----
        children = all previously stored folds
        """
        children = []
        with open(pickle_file, 'rb') as file:
            while True:
                try:
                    fold = pickle.load(file)
                    children.append(fold)
                except EOFError:
                    break
                
        return children
        
    
    def determine_best_fold(self) -> object:
        """
        iterates over stored results and saves the best fold
        
        Output:
        ----
        best_fold = the best fold found
        """
        # read results file and return best folds
        best_score = 1
        best_fold = None
        
        with open(self.filename, 'rb') as file:
            while True:
                try:
                    fold = pickle.load(file)
                    if fold.score < best_score:
                        best_fold = fold
                        best_score = fold.score
                    else:
                        continue
                except EOFError:
                    break
                
        return best_fold
    
    
    def create_ancestor(self) -> object:
        """
        Creates the beginning fold to start the depth-first search
        
        Output:
        ----
        ancestor = parent fold with two aminoacids
        """
        # creates initial fold from which all other child folds are created
        coordinate1 = (0,0)
        coordinate2 = (0,1)
        amino1 = Aminoacid(0, self.Protein.protein[0])
        amino1.set_current_coordinate(coordinate1)
        amino1.set_next_coordinate(coordinate2)
        amino2 = Aminoacid(1, self.Protein.protein[1])
        amino2.set_previous_coordinate(coordinate1)
        amino2.set_current_coordinate(coordinate2)
        
        ancestor = Fold(self.fold_counter, self.Protein.protein, [amino1, amino2], [coordinate1, coordinate2])
        return ancestor
    
    
    def check_protein(self, children: list):
        """
        asserts if the Protein being folded by the pickled data matches the Protein wanting to be folded
        """
        child = children[0]
        child_protein = child.protein
        assert child_protein == self.Protein.protein, "The protein you provided is not the same as the protein that was previously used"