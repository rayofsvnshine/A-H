"""
visualisation.py

* Creates a visualization of the protein
"""

import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


class Visualisation:
    """
    Class containing functions to create a 2D or 3D visualisation of the best folded protein.
    """

    def __init__(self, bestfold: object):
        """
        Initializer
        """

        self.all_coordinates = bestfold.coordinates
        self.p_coordinates = self.get_p_coordinates(bestfold)
        self.h_coordinates = self.get_h_coordinates(bestfold)
        self.c_coordinates = self.get_c_coordinates(bestfold)


    def get_p_coordinates(self, bestfold: object) -> list:
        """
        Get all coordinates from the P amino acids.

        Pre:
            Bestfold is an object containing the coordinates and the matching aminotypes in the best fold.
        Post:
            Returns a list of tuples representing the coordinates of all P amino acids.
        """

        p_coordinates = []

        # Filter P amino acids
        for aminoacid in bestfold.aminoacids:
            if aminoacid.aminotype == "P":
                p_coordinates.append(aminoacid.coordinate)

        return p_coordinates


    def get_h_coordinates(self, bestfold: object) -> list:
        """
        Get all coordinates from the H amino acids.

        Pre:
            Bestfold is an object containing the coordinates and the matching aminotypes in the best fold.
        Post:
            Returns a list of tuples representing the coordinates of all H amino acids.
        """

        h_coordinates = []

        # Filter H amino acids
        for aminoacid in bestfold.aminoacids:
            if aminoacid.aminotype == "H":
                h_coordinates.append(aminoacid.coordinate)

        return h_coordinates


    def get_c_coordinates(self, bestfold: object) -> list:
        """
        Get all coordinates from the C amino acids.

        Pre:
            Bestfold is an object containing the coordinates and the matching aminotypes in the best fold.
        Post:
            Returns a list of tuples representing the coordinates of all C amino acids.
        """

        c_coordinates = []

        # Filter H amino acids
        for aminoacid in bestfold.aminoacids:
            if aminoacid.aminotype == "C":
                c_coordinates.append(aminoacid.coordinate)

        return c_coordinates


    def visualize_protein_plotly_3d(self) -> None:
        """
        Creates a 3D visualization of the protein using plotly.

        Pre:
            Uses a list of tuples with all the coordinates of the best fold and uses
            a list of tuples with all the coordinates of the p, h and c amino acids.
        Post:
            Returns a dynamic visualization of the best fold.
        """

        # Load the x, y and z coordinates for the protein structure
        x = []
        y = []
        z = []
        for coordinate in self.all_coordinates:
            x.append(coordinate[0])
            y.append(coordinate[1])
            z.append(0)

        # Create 3D protein structure
        structure = px.line_3d(x = x, y = y, z = z)
        structure.update_traces(line = dict(color = "black", width = 8))

        # Load the x, y and z coordinates of the P amino acids
        p_x = []
        p_y = []
        p_z = []
        for coordinate in self.p_coordinates:
            p_x.append(coordinate[0])
            p_y.append(coordinate[1])
            p_z.append(0)

        # Create amino acid locations for P
        p = go.Figure(data = go.Scatter3d(x = p_x,
                                          y = p_y,
                                          z = p_z,
                                          mode = "markers",
                                          name = "Polair (P)",
                                          marker = dict(size = 15,
                                                        color = "blue",
                                                        opacity = 0.5)))

        # Load the x, y and z coordinates of the H amino acids
        h_x = []
        h_y = []
        h_z = []
        for coordinate in self.h_coordinates:
            h_x.append(coordinate[0])
            h_y.append(coordinate[1])
            h_z.append(0)

        # Create amino acid locations for H
        h = go.Figure(data = go.Scatter3d(x = h_x,
                                          y = h_y,
                                          z = h_z,
                                          mode = "markers",
                                          name = "Hydrofobe (H)",
                                          marker = dict(size = 15,
                                                        color = "red",
                                                        opacity = 0.5)))

        # Load the x, y and z coordinates of the C amino acids
        c_x = []
        c_y = []
        c_z = []
        for coordinate in self.c_coordinates:
            c_x.append(coordinate[0])
            c_y.append(coordinate[1])
            c_z.append(0)

        # Create amino acid locations for C
        c = go.Figure(data = go.Scatter3d(x = c_x,
                                          y = c_y,
                                          z = c_z,
                                          mode = "markers",
                                          name = "Cysteine (C)",
                                          marker = dict(size = 15,
                                                        color = "green",
                                                        opacity = 0.5)))

        # Combine all protein data
        protein = go.Figure(data = structure.data + p.data + h.data + c.data)

        # Layout
        protein.update_layout(scene = dict(xaxis = dict(color="white", showbackground=False),
                                           yaxis = dict(color="white", showbackground=False),
                                           zaxis = dict(color="white", showbackground=False)),
                              legend_title = "Amino acid",
                              legend_font_size= 20)

        # protein = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z)],
        #                     layout=go.Layout(xaxis=dict(range=[0, 5], autorange=False),
        #                                      yaxis=dict(range=[0, 5], autorange=False),
        #                                      updatemenus=[dict(type="buttons",
        #                                                        buttons=[dict(label="Create protein",
        #                                                                      method="animate",
        #                                                                      args=[None])])]),
        #                     frames=[go.Frame(data=[go.Scatter3d(x=[x[0]], y=[y[0]], z=[z[0]])]),
        #                             go.Frame(data=[go.Scatter3d(x=[x[1]], y=[y[1]], z=[z[1]])])
        #                             ])

        # Show protein
        protein.show()


    # def visualize_protein_plotly_2d(self) -> None:
    #     """
    #     Creates a 2D visualization of the protein using plotly.

    #     Pre:
    #         Uses a list of tuples with all the coordinates of the best fold.
    #     Post:
    #         Returns a dynamic visualization of the best fold.
    #     """

    #     # creating x,y dimension
    #     x = []
    #     y = []

    #     # Insert the coordinate into the protein plot
    #     for coordinate in bestfold.coordinates:
    #         x.append(coordinate[0])
    #         y.append(coordinate[1])

    #     # Create 2D plot
    #     fig = px.line(x = x, y = y, markers = True)

    #     # Hide x and y axis
    #     fig.update_xaxes(visible = False)
    #     fig.update_yaxes(visible = False)

    #     # Remove background
    #     fig.update_layout(template = "simple_white")

    #     # Show protein
    #     fig.show()


    # def visualize_protein_matplotlib(bestfold):
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

    #     # Create title
    #     plt.title(f"Best fold:")

    #     # Showing the plot
    #     plt.show()
