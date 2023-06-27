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


    def algorithm_comparison(random, FRESS, pruning) -> None:
        """
        Displays a histogram to show the performance of all algorithms.

        Pre:
            Uses a list with all protein folds.
        Post:
            Shows a performance histogram for all algorithms.
        """

        # Get max length
        length_random = max(random) - min(random) + 1
        length_FRESS = max(FRESS) - min(FRESS) + 1
        length_pruning = max(pruning) - min(pruning) + 1
        length = max(length_random, length_FRESS, length_pruning)

        # Create a histogram
        histogram = go.Figure()
        histogram.add_trace(go.Histogram(x = random, name = "Random", nbinsx = length))
        histogram.add_trace(go.Histogram(x = FRESS, name = "FRESS", nbinsx = length))
        histogram.add_trace(go.Histogram(x = pruning, name = "Pruning", nbinsx = length))

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

        # Create a legend
        histogram.update_layout(legend_font_size = 25,
                                legend = dict(orientation = "h",
                                              xanchor = "center",
                                              x = 0.5))

        # Add line
        histogram.add_vline(x = -2, line_color = 'firebrick')

        # Display the histogram
        histogram.show()
