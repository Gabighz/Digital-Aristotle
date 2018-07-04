##################################################
# Main program which executes the modules,       #
# and writes Keywords and Non-keywords to a file #
##################################################

# This constant is used in kmeans.py. It determines the number of classifications.
# Currently, we have 2 classifications, namely Keywords and Non-keywords.
CLUSTERS = 2

import os

from XML_parser import parse_file
from feature_selection import feature_assignment
from kmeans import kmeans_clustering
from processing import pre_processing, post_processing

def main():
    # Open a file here and apply a function from XML_parser to it
    path = '../input/foundation-year/CSC079/Slides-Week-2.xml'
    file_number = 0 
    parsed_content = parse_file(path, file_number)

    # Pre-processing to filter out stopwords from parsed_files
    filtered_content = pre_processing(parsed_content)

    # Return a two-dimensional array which contains each word and its features
    classification_features = feature_assignment(filtered_content)

    # Prints each word and its classification features
    print("\n \n Each word and its classification features: \n")
    for word in classification_features:
        # Format and content: [word, isBold, isBig, isAbnormalColour, RAKE]
        print(word)

    # The return is 2D array which contains each word and its label
    clustered_data = kmeans_clustering(classification_features, CLUSTERS)

    # Post-processing to measure the performance of our classifier
    performance = post_processing(clustered_data)
    print("F1 score: ", performance)

    # Write to file
    path = "../output/foundation-year/CSC079/SlidesWeek2.txt"

    # Enables us to create paths from within the program
    os.makedirs(os.path.dirname(path), exist_ok=True)

    file = open(path, "w")

    for observation in clustered_data:
        file.write(str(observation) + "\n")

    file.close()

main()
