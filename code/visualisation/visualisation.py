"""
visualisation.py

* Creates a visualization of the protein
"""

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
        self.hydrogen_bonds = self.get_hydrogen_bonds(bestfold)


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


    def get_hydrogen_bonds(self, bestfold) -> list:
        """
        Finds the two coordinates of the hydrogen bond.

        Pre:
            ...
        Post:
            ...
        """

        # Make a list to store all hydrogen bonds
        hydrogen_bonds = []
        
        # Loop over all aminoacids
        for aminoacid in bestfold.aminoacids:

            # Check the neighbours of all H and C amino acids
            if aminoacid.aminotype == 'H' or aminoacid.aminotype == 'C':

                # Create neighbour list
                neighbours = []

                # Get x and y of current coordinate
                current_x = aminoacid.coordinate[0]
                current_y = aminoacid.coordinate[1]

                # Loop over all coordinates of the amino acids
                for coordinate in bestfold.coordinates:
                    x = coordinate[0]
                    y = coordinate[1]
            
                    # If the coordinates are neighbouring, add them to neighbours
                    if current_x + 1 == x and current_y == y:
                        neighbours.append(coordinate)
                    elif current_x - 1 == x and current_y == y:
                        neighbours.append(coordinate)
                    elif current_y + 1 == y and current_x == x:
                        neighbours.append(coordinate)
                    elif current_y - 1 == y and current_x == x:
                        neighbours.append(coordinate)
            
                # Check for aminoacid
                for neighbour in neighbours:
                    ind = bestfold.coordinates.index(neighbour)
                    neighbour_obj = bestfold.aminoacids[ind]

                    # If both H or C aminoacids are not already checked, store coordinates for H-bond
                    if neighbour_obj.aminotype == 'H' or neighbour_obj.aminotype == 'C':
                        if neighbour_obj.id >= aminoacid.id + 2:
                            hydrogen_bond = []
                            hydrogen_bond.append(aminoacid.coordinate)
                            hydrogen_bond.append(neighbour_obj.coordinate)
                            hydrogen_bonds.append(hydrogen_bond)

        return hydrogen_bonds


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

        # Add structure to data
        all_data = structure.data

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
                                                        opacity = 0.6)))

        # Add P to data
        all_data += p.data

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
                                                        opacity = 0.6)))

        # Add H to data
        all_data += h.data

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
                                                        opacity = 0.6)))

        # Add C to data
        all_data += c.data

        # Create coordinates to display hydrogen bonds
        for hydrogen_bond in self.hydrogen_bonds:
            hyd_x = []
            hyd_y = []
            hyd_z = []
            for coordinate in hydrogen_bond:
                hyd_x.append(coordinate[0])
                hyd_y.append(coordinate[1])
                hyd_z.append(0)

            # Create 3D hydrogen bond and store to data
            hyd_bond = px.line_3d(x = hyd_x, y = hyd_y, z = hyd_z)
            hyd_bond.update_traces(line = dict(color = "black", width = 13, dash = "dot"))
            all_data += hyd_bond.data

        # Create a protein
        protein = go.Figure(data = all_data)

        # Remove the axes
        protein.update_layout(scene = dict(xaxis = dict(color="white", showbackground=False),
                                           yaxis = dict(color="white", showbackground=False),
                                           zaxis = dict(color="white", showbackground=False)))

        # Create a legend
        protein.update_layout(legend_font_size= 25,
                              legend=dict(orientation = "h",
                                    xanchor = "center",
                                    x = 0.5))

        # Show the protein
        protein.show()
