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
    # open a file here and apply a function from XMLParser to it

    # apply a function from FeatureSelection to the return of the aforementioned function
    # and return a two-dimensional array which contains each word and its features

    # apply K-means clustering to the aforementioned array

main()
