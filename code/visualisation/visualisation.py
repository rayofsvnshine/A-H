"""
visualisation.py

* Creates a visualization of the protein
"""

# Import main
from main import *

# Imports for matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Imports for plotly
import plotly.express as px
from dash import Dash, dcc, html, Input, Output


def visualize_protein(bestfold):
    """
    Creates a dynamic visualization of the protein using plotly.

    Pre:
        Uses a list of tuples with all the coordinates of the best fold.
    Post:
        Returns a dynamic visualization of the best fold.
    """

    # creating a x,y and z dimension
    x = []
    y = []
    z = []

    # Insert the coordinate into the protein plot
    for coordinate in bestfold.coordinates:
        x.append(coordinate[0])
        y.append(coordinate[1])
        z.append(0)
    
    # fig = px.scatter_3d(x = x,
    #                     y = y,
    #                     z = z)
    
    fig = px.line_3d(x = x,
                        y = y,
                        z = z,
                        markers = True)

    fig = px.line(x = x,
                  y = y,
                  markers = True)

    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)

    fig.update_layout(template='simple_white')

    fig.show()

    # data = px.data.iris()

    # fig = px.scatter_3d(data, x='sepal_length', y='sepal_width', z='petal_width', color='species')

    # fig.update_layout(showlegend=False)
    # fig.update_xaxes(visible=False)
    # fig.update_yaxes(visible=False)
    # fig.update_xaxes(showgrid=False)
    # fig.update_yaxes(showgrid=False)

    # fig.update_layout(template='simple_white')

    # fig.show()


# def visualize_protein(bestfold):
#     """
#     Creates a visualization of the protein using matplotlib.

#     Pre:
#         Uses a list of tuples with all the coordinates of the best fold.
#     Post:
#         Returns a visualization of the best fold.
#     """

#     # creating an empty canvas
#     fig = plt.figure()

#     # defining the axes with the projection as 3D so as to plot 3D graphs
#     ax = plt.axes(projection="3d")

#     # creating a x,y and z dimension
#     x = []
#     y = []
#     z = []

#     # Insert the coordinate into the protein plot
#     for coordinate in bestfold.coordinates:
#         x.append(coordinate[0])
#         y.append(coordinate[1])
#         z.append(0)

#     # plotting a 3D line graph with X-coordinate, Y-coordinate and Z-coordinate respectively
#     ax.plot3D(x, y, z, "k")

#     # plotting the protein
#     ax.scatter3D(x, y, z, c=z, cmap="Dark2_r", edgecolor="k", s = 2000);

#     #specify axis tick step sizes
#     plt.xticks(np.arange(min(x), max(x)+1, 1))
#     plt.yticks(np.arange(min(y), max(y)+1, 1))

#     #get current axes
#     ax = plt.gca()

#     # Hide axes and borders
#     plt.axis("off")

#     # Showing the plot
#     plt.title(f"Optimum protein fold")
#     plt.show()