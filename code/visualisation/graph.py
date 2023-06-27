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


    def algorithm_performance(self, algorithm_name) -> None:
        """
        Displays a histogram to show the performance of the algorithm.

        Pre:
            Uses a list with all protein folds.
        Post:
            Shows a histogram.
        """

        # Get length
        length = max(self.scores) - min(self.scores) + 1

        # Create a histogram
        histogram = px.histogram(x = self.scores, nbins = length)

        # Update x-axis
        histogram.update_xaxes(tickmode = "array",
                               tickvals = self.scores)
        # Update the layout
        histogram.update_layout(title_text = f"{algorithm_name} algorithm performace",
                                title_x = 0.5,
                                font = dict(size = 24),
                                bargap = 0.01,
                                xaxis_title = "Score",
                                yaxis_title = "Count")

        # Display the histogram
        histogram.show()


    # def algorithm_comparison(data) -> None:
    #     """
    #     Displays a histogram to show the performance of all algorithms.

    #     Pre:
    #         Uses a list with all protein folds.
    #     Post:
    #         Shows a performance histogram for all algorithms.
    #     """

    #     # Create a histogram
    #     histogram = go.Figure()

    #     # Extract data
    #     for list in data:
    #         histogram.add_trace(go.Histogram(x = list))

    #     # Update the layout
    #     histogram.update_layout(barmode = "overlay",
    #                             title_text = "Algorithm performace comparison",
    #                             title_x = 0.5,
    #                             font = dict(size = 24),
    #                             bargap = 0.01,
    #                             xaxis_title = "Score",
    #                             yaxis_title = "Count")

    #     # Reduce opacity to see both histograms
    #     histogram.update_traces(opacity = 0.75)

    #     # Display the histogram
    #     histogram.show()


    def algorithm_comparison(random, FRESS, pruning,) -> None:
        """
        Displays a histogram to show the performance of all algorithms.

        Pre:
            Uses a list with all protein folds.
        Post:
            Shows a performance histogram for all algorithms.
        """

        # Create a histogram
        histogram = go.Figure()
        histogram.add_trace(go.Histogram(x = random))
        histogram.add_trace(go.Histogram(x = FRESS))
        histogram.add_trace(go.Histogram(x = pruning))

        # Update the layout
        histogram.update_layout(barmode = "overlay",
                                title_text = "Algorithm performace comparison",
                                title_x = 0.5,
                                font = dict(size = 24),
                                bargap = 0.01,
                                xaxis_title = "Score",
                                yaxis_title = "Count")

        # Reduce opacity to see both histograms
        histogram.update_traces(opacity = 0.75)

        # Display the histogram
        histogram.show()
