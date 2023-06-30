"""
graph.py
    * Creates a histogram to visualise the performance of the algorithm.
    * Creates a histogram to compare the performance of multiple algorithms.
"""

import plotly.express as px
import plotly.graph_objects as go


class Graph:
    """
    A class for creating and displaying histograms to visualize algorithm performance.
    """

    def __init__(self, proteinfolds: object) -> None:
        """
        Initializes a Graph object.

        Pre:
            proteinfolds (List): A list of protein folds.
        """

        self.proteinfolds = proteinfolds
        self.scores = [fold.score for fold in self.proteinfolds]

    def algorithm_performance(self, algorithm_name: str) -> None:
        """
        Creates and displays a histogram to visualize the algorithm performance.

        Pre:
            The proteinfolds attribute is initialized with valid protein folds.
            Algorithm_name is a string that contains the name of the algorithm.

        Post:
            A histogram is displayed to visualize the algorithm performance.
        """

        # Get the length of all scores
        length = max(self.scores) - min(self.scores) + 1

        # Create a histogram
        histogram = px.histogram(x=self.scores, nbins=length)

        # Update x-axis tick distance
        histogram.update_xaxes(tickmode="array", tickvals=self.scores)

        # Update the layout of the histogram
        histogram.update_layout(
            title_text=f"{algorithm_name} algorithm performace",
            title_x=0.5,
            font=dict(size=24),
            bargap=0.01,
            xaxis_title="Score",
            yaxis_title="Count",
        )

        # Display the histogram
        histogram.show()

    def algorithm_comparison(random: list, FRESS: list, greedy: list) -> None:
        """
        Creates and displays a histogram to compare the performance of different algorithms.

        Pre:
            The parameter random is a list containing the scores of the random algorithm.
            The parameter FRESS is a list containing the scores of the FRESS algorithm.
            The parameter greedy is a list containing the scores of the greedy algorithm.

        Post:
            A histogram is displayed to compare the performance of different algorithms.
        """

        # Get max length
        length_random = max(random) - min(random) + 1
        length_FRESS = max(FRESS) - min(FRESS) + 1
        length_greedy = max(greedy) - min(greedy) + 1
        length = max(length_random, length_FRESS, length_greedy)

        # Create a histogram
        histogram = go.Figure()
        histogram.add_trace(go.Histogram(x=random, name="Random", nbinsx=length))
        histogram.add_trace(go.Histogram(x=FRESS, name="FRESS", nbinsx=length))
        histogram.add_trace(go.Histogram(x=greedy, name="Greedy", nbinsx=length))

        # Update the layout of the histogram
        histogram.update_layout(
            barmode="overlay",
            title_text="Algorithm performace comparison",
            title_x=0.5,
            font=dict(size=24),
            bargap=0.01,
            xaxis_title="Score",
            yaxis_title="Count",
        )

        # Reduce opacity to see both histograms
        histogram.update_traces(opacity=0.75)

        # Create a legend
        histogram.update_layout(
            legend_font_size=25, legend=dict(orientation="h", xanchor="center", x=0.5)
        )

        # Display the histogram
        histogram.show()
