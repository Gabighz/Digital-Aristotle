##################################################
# Main program which executes the modules,       #
# handles pre-processing and post-processing,    #
# and writes Keywords and Non-keywords to a file #
# (Gabriel Ghiuzan)                              #
##################################################

CLUSTERS = 2

# to be changed with functions where necessary
from .XMLParser import *
from .FeatureSelection import *
from .KMeans import *

def main():
    # Open a file here and apply a function from XMLParser to it

    # Apply a function from FeatureSelection to the return of the aforementioned function.
    # Return a two-dimensional array which contains each word and its features, named word_list

    # Apply K-means clustering to the aforementioned array
    kmeans_clustering(word_list, CLUSTERS)

main()
