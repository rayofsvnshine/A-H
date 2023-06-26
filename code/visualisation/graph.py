"""
graphs.py

* Creates a graph visualization of the performance of the random algorithm
"""

import plotly.express as px
import plotly.graph_objects as go


class Graph:
    """
    Class containing functions to create performance graphs.
    """

    def __init__(self, proteinfolds):
        """
        Initializer
        """

        self.proteinfolds = proteinfolds
        self.scores = [fold.score for fold in self.proteinfolds]


    def algorithm_performance(self) -> None:
        """
        Displays a histogram to show the performance of the algorithm.

        Pre:
            Uses a list with all protein folds.
        Post:
            Shows a histogram.
        """

        # Create a histogram
        histogram = px.histogram(x = self.scores)

        # Update x-axis
        histogram.update_xaxes(tickmode = 'array',
                               tickvals = self.scores)
        # Update the layout
        histogram.update_layout(title_text='Algorithm performace score count',
                                title_x = 0.5,
                                font = dict(size = 24),
                                bargap = 0.01,
                                xaxis_title = "Score",
                                yaxis_title = "Count",
                                xaxis_categoryorder = 'total ascending')

        # Display the histogram
        histogram.show()
