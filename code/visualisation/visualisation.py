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


    # Creating an empty plot
    fig = plt.figure()

    # Defining the axes as a 3D axes so that we can plot 3D data into it
    ax = plt.axes(projection="3d")

    X = [1,2,3]
    Y = [1,2,2]
    Z = [1,2,3]

    ax.scatter(X, Y, Z)

    # Showing the above plot
    plt.show()


    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection="3d")

    # X = [1,2,3,4,5,6,7,8,9,10]
    # Y = [1,2,2,4,5,2,7,8,1,4]
    # Z = [1,2,3,4,5,6,7,8,9,10]

    # ax.scatter(X, Y, Z, c="r", marker="o")

    # plt.show()