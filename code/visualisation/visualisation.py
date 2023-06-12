""" visualisation.py """

import matplotlib.pyplot as plt
import numpy as np
from main import *

def make_plot(best_fold):
    """ Function that will return a graph with the best fold."""

    # for i in range(len(best_fold.coordinates)):
    #    txt = best_fold.aminoacids[i].aminotype
    #    print(txt)
    #    plt.plot(best_fold.coordinates[i], color = 'blue')
    #    plt.annotate(txt, best_fold.coordinates[i])
    # plt.plot(best_fold.coordinates)
    # txt = best_fold.aminoacids.aminotype
    # plt.annotate(txt, best_fold.coordinates)
    # plt.title('Protein fold')
    # plt.show()

    # for coordinate in best_fold.coordinates:
    #     print(best_fold.coordinates)
    #     break

    # creating an empty canvas
    fig = plt.figure()

    # defining the axes with the projection as 3D so as to plot 3D graphs
    ax = plt.axes(projection="3d")

    # creating a wide range of points x,y,z
    x = [0,1,1,2,2,3,3,4,4,5,5]
    y = [0,0,1,1,2,2,3,3,4,4,5]
    z = [0,0,0,0,0,0,0,0,0,0,0]

    # for coordinate 
    # x = [0,1,1,2,2,3,3,4,4,5,5]
    # y = [0,0,1,1,2,2,3,3,4,4,5]
    # z = [0,0,0,0,0,0,0,0,0,0,0]

    # plotting a 3D line graph with X-coordinate, Y-coordinate and Z-coordinate respectively
    ax.plot3D(x, y, z, "k")

    # plotting a scatter plot with X-coordinate, Y-coordinate and Z-coordinate respectively
    # and defining the points color as cividis and defining c as z which basically is a
    # definition of 2D array in which rows are RGB or RGBA
    ax.scatter3D(x, y, z, c=z, cmap="Dark2_r", edgecolor="k", s = 2000);

    #get current axes
    ax = plt.gca()

    # Hide axes and borders
    plt.axis("off")

    # Showing the plot
    plt.title(f"Optimum protein fold")
    plt.show()
