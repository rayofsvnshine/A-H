"""
visualisation.py

* Creates a visualization of the protein
"""

import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


class Visualisation:

    def visualize_protein_plotly_3d(bestfold):
        """
        Creates a 3D visualization of the protein using plotly.

        Pre:
            Uses a list of tuples with all the coordinates of the best fold.
        Post:
            Returns a dynamic visualization of the best fold.
        """

        # creating x,y and z dimension
        x = []
        y = []
        z = []

        # Insert all coordinates into the protein structure
        for coordinate in bestfold.coordinates:
            x.append(coordinate[0])
            y.append(coordinate[1])
            z.append(0)

        # Create 3D protein structure
        structure = px.line_3d(x = x, y = y, z = z)

        # creating x,y and z dimension for P
        p_x = []
        p_y = []
        p_z = []

        # Insert the P coordinates into the protein structure
        for coordinate in bestfold.coordinates:
            x.append(coordinate[0])
            y.append(coordinate[1])
            z.append(0)

        # Show amino acid locations for P
        p = px.scatter_3d(x = p_x, y = p_y, z = p_z)

        # creating x,y and z dimension for H
        h_x = []
        h_y = []
        h_z = []

        # Show amino acid locations for H
        h = px.scatter_3d(x = h_x, y = h_y, z = h_z)

        # creating x,y and z dimension for H
        c_x = []
        c_y = []
        c_z = []

        # Show amino acid locations for C
        c = px.scatter_3d(x = c_x, y = c_y, z = c_z)

        # Combine protein data
        protein = go.Figure(data = structure.data + p.data + h.data + c.data)

        # Show protein
        protein.show()


    def visualize_protein_plotly_2d(bestfold):
        """
        Creates a 2D visualization of the protein using plotly.

        Pre:
            Uses a list of tuples with all the coordinates of the best fold.
        Post:
            Returns a dynamic visualization of the best fold.
        """

        # creating x,y dimension
        x = []
        y = []

        # Insert the coordinate into the protein plot
        for coordinate in bestfold.coordinates:
            x.append(coordinate[0])
            y.append(coordinate[1])

        # Create 2D plot
        fig = px.line(x = x, y = y, markers = True)

        # Hide x and y axis
        fig.update_xaxes(visible = False)
        fig.update_yaxes(visible = False)

        # Remove background
        fig.update_layout(template = "simple_white")

        # Show protein
        fig.show()


    def visualize_protein_matplotlib(bestfold):
        """
        Creates a visualization of the protein using matplotlib.

        Pre:
            Uses a list of tuples with all the coordinates of the best fold.
        Post:
            Returns a visualization of the best fold.
        """

        # creating an empty canvas
        fig = plt.figure()

        # defining the axes with the projection as 3D so as to plot 3D graphs
        ax = plt.axes(projection="3d")

        # creating a x,y and z dimension
        x = []
        y = []
        z = []

        # Insert the coordinate into the protein plot
        for coordinate in bestfold.coordinates:
            x.append(coordinate[0])
            y.append(coordinate[1])
            z.append(0)

        # plotting a 3D line graph with X-coordinate, Y-coordinate and Z-coordinate respectively
        ax.plot3D(x, y, z, "k")

        # plotting the protein
        ax.scatter3D(x, y, z, c=z, cmap="Dark2_r", edgecolor="k", s = 2000);

        #specify axis tick step sizes
        plt.xticks(np.arange(min(x), max(x)+1, 1))
        plt.yticks(np.arange(min(y), max(y)+1, 1))

        #get current axes
        ax = plt.gca()

        # Hide axes and borders
        plt.axis("off")

        # Create title
        plt.title(f"Best fold:")

        # Showing the plot
        plt.show()


        # ----------------------------------------- PLOTLY LAYOUT -----------------------------------------
        # Markers
        # fig = go.Figure(data=go.Scatter3d(x=x, y=y, z=z, marker=dict(size=20, color="blue"),
        #                                                  line=dict(
        #                                                  color="black",
        #                                                  width=5)))

        # Layout
        # fig.update_layout(scene = dict(xaxis = dict(color="white", showbackground=False),
        #                                yaxis = dict(color="white", showbackground=False),
        #                                zaxis = dict(color="white", showbackground=False)))

        # fig.update_layout(scene = dict(
        #             xaxis = dict(
        #                  color="white",
        #                  backgroundcolor="white",
        #                  gridcolor="white",
        #                  showbackground=True,
        #                  zerolinecolor="white",),
        #             yaxis = dict(
        #                 color="white",
        #                 backgroundcolor="white",
        #                 gridcolor="white",
        #                 showbackground=True,
        #                 zerolinecolor="white"),
        #             zaxis = dict(
        #                 color="white",
        #                 backgroundcolor="white",
        #                 gridcolor="white",
        #                 showbackground=True,
        #                 zerolinecolor="white")))
