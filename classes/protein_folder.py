"""
protein_folder.py
Folder class

Parameters:
------
Protein chain (String)

Returns:
------
Various folds of the protein chain
List of tuples with directions

------
* folds protein according to certain criteria:
    * no overlap on 2D grid
    * folds are done with 90 degree angles
    * check if the next space allows further movement
    * if movement is stunted, invalid fold
* stores coordinates of aminoacids
"""

class Folder:

    def __init__(self):
        self.thing = 0