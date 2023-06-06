"""
scoring.py

Parameters:
-------
List of tuples with directions

Returns:
-------
CSV with optimal protein coordinates (tuples) and score


* 
* counts the scores for each H-connection
* counts the scores for each C-connection (if present)
* gives a total score for each fold
* compares total scores of different proteins to determine the optimal fold
"""


class Score:

    def __init__(self):
        self.stuff = 1