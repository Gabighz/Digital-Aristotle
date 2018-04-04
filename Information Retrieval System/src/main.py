##################################################
# Main program which executes the modules,       #
# handles pre-processing and post-processing,    #
# and writes Keywords and Non-keywords to a file #
##################################################

CLUSTERS = 2

# to be changed with functions where necessary
from XML_parser import *
from feature_selection import *
from kmeans import kmeans_clustering

def main():
    # Open a file here and apply a function from XML_parser to it

    path = '../input/foundation-year/CSC079/Slides-Week-2.xml' # to be changed to something more flexible in the future
    parsed_files = XML_parser()
    parsed_files.parse_file(path)

    selected_features = feature_selection(parsed_files.get_parsed_words()) # to be changed to something pythonic

    var = assignedFeatures.getWordList() # what is var? please use meaningful identifier names
    for e in var: # what is e?
        print(e)

    # Apply a function from feature_selection to the return of the aforementioned function.
    # Return a two-dimensional array which contains each word and its features, named word_list

    # Apply K-means clustering to the aforementioned array
    kmeans_clustering(word_list, CLUSTERS)

main()
