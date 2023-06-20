"""
graphs.py

* Creates a graph visualization of the performance of the random algorithm
"""

import plotly.express as px


class Graph:
    """
    Class containing functions to create performance graphs.
    """

    def __init__(self):
        """
        Initializer
        """

        self.random = []


    def algorithm_performance(self) -> None:
        """
        ...

        Pre:
            ...
        Post:
            ...
        """

        df = px.data.tips()
        fig = px.histogram(df, x="total_bill")
        fig.show()
