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
        histogram = go.Figure()

        # Add labels
        histogram.add_trace(go.Histogram(x=self.scores,
                                         name = "Count",
                                         texttemplate = "%{x}",
                                         textfont_size = 20))

        # Hide x-axis
        histogram.update_xaxes(visible=False)

        # Update the layout
        histogram.update_layout(title = "Protein folding scores using a random algorithm",
                                font=dict(size = 22))

        # Display the histogram
        histogram.show()
