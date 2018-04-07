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

    path = '../input/foundation-year/CSC079/*.xml'
    parsed_files = XML_parser()
    parsed_files.parse_file(path)

    # Apply a function from feature_selection to the return of the aforementioned function.
    # Return a two-dimensional array which contains each word and its features, named word_list
    # !! To be changed to a single 'interface' function, in a pythonic way

    selected_features = feature_selection(parsed_files.get_parsed_words())

    var = selected_features.get_word_list() # what is var? please use meaningful identifier names
    for e in var: # what is e?
        print(e)

    # Apply K-means clustering to the aforementioned array
    # At the moment, the return is a data collection of the labels of each point
    labels = kmeans_clustering(word_list, CLUSTERS)

    # Write to file
    file = open("keywords.txt", "r")

    for label in labels:
        file.write(label)

    file.close()

main()
