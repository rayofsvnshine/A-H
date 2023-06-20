"""
graphs.py

* Creates a graph visualization of the performance of the random algorithm
"""

import plotly.express as px


class Graph:
    """
    Class containing functions to create performance graphs.
    """

    def __init__(self, proteinfolds):
        """
        Initializer
        """

        self.proteinfolds = proteinfolds


    def algorithm_performance(self) -> None:
        """
        Displays a histogram to show the performance of the algorithm.

        Pre:
            Uses a list with all protein folds.
        Post:
            Shows a histogram.
        """

        df = px.data.tips()
        print(df)
        performance = px.histogram(df, x="total_bill")
        performance.show()
