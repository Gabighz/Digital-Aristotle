##################################################
# Main program which executes the modules,       #
# and writes Keywords and Non-keywords to a file #
##################################################

CLUSTERS = 2

import os

from XML_parser import parse_file
from feature_selection import feature_assignment
from kmeans import kmeans_clustering
from processing import post_processing

def main():
    # Open a file here and apply a function from XML_parser to it

    path = '../input/foundation-year/CSC079/Slides-Week-2.xml'
    file_number = 0
    parsed_files = parse_file(path, file_number)

    # Pre-processing to filter out stopwords from parsed_files


    # Apply a function from feature_selection to the return of the aforementioned function.
    # Return a two-dimensional array which contains each word and its features

    selected_features = feature_assignment(parsed_files)

    #prints off each entry in the selected features array(purely for debugging and demonstration not needed)
    for e in selected_features:
        print(e)

    # Apply K-means clustering to the aforementioned array
    # The return is 2D array which contains each word and its label
    clustered_data = kmeans_clustering(selected_features, CLUSTERS)

    # Post-processing to measure the performance of our classifier
    performance = post_processing(clustered_data)

    print("F1 score: ", performance)

    # Write to file
    path = "../output/foundation-year/CSC079/SlidesWeek2.txt"

    os.makedirs(os.path.dirname(path), exist_ok=True) # enables us to create paths from within the program

    file = open(path, "w")

    for observation in clustered_data:

        file.write(str(observation) + "\n")

    file.close()

main()
